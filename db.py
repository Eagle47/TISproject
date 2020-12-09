from sqlalchemy import create_engine, text


class DB(object):
  def __init__(self):
    self.engine = create_engine('sqlite:///data.db', echo = True)

  ### MUSEUMS ###

  def get_museums(self):
    query = text('SELECT * FROM museums')
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output


  def get_museum_info(self, museum_id):
    query = text('SELECT name, foundation_year, city FROM museums WHERE id =' + museum_id)
    query_result = self.engine.execute(query)
   
    output = []
    for row in query_result:
      output.append(dict(row))

    return output[0]


  def get_exhibits_for_museum(self, museum_id):
    query = text('SELECT e.name AS exhibit, type, creation_year FROM exhibits e JOIN museums_exhibits me JOIN museums m ON e.id = me.id_exhibit AND m.id = me.id_museum WHERE me.id_museum =' + museum_id)
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output


  def add_museum(self, name, foundation_year, city):
    query = text('INSERT INTO museums VALUES (NULL, "' + str(name) + '", "' + str(foundation_year) + '", "' + str(city) + '")')
    query_result = self.engine.execute(query)


  def remove_museum(self, name):
    query = text('DELETE FROM museums WHERE name = "' + name + '"')
    query_result = self.engine.execute(query)

  
  def add_exhibit_to_museum(self, museum_name, exhibit_name):
    query = text('INSERT INTO museums_exhibits VALUES ((SELECT id FROM museums WHERE name = "' + str(museum_name) + '"), (SELECT id FROM exhibits WHERE name = "' + str(exhibit_name) + '"))')
    query_result = self.engine.execute(query)  

  
  def remove_exhibit_from_museum(self, exhibit_name):
    query = text('DELETE FROM museums_exhibits WHERE id_exhibit = (SELECT id FROM exhibits WHERE name = "' + exhibit_name + '")')
    query_result = self.engine.execute(query)



  ### EXHIBITS ###

  def get_exhibits(self):
    query = text('SELECT * FROM exhibits')
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output


  def add_exhibit(self, name, typ, creation_year):
    query = text('INSERT INTO exhibits VALUES (NULL, "' + str(name) + '", "' + str(typ) + '", "' + str(creation_year) + '")')
    query_result = self.engine.execute(query)


  def remove_exhibit(self, name):
    query = text('DELETE FROM exhibits WHERE name = "' + name + '"')
    query_result = self.engine.execute(query)


  ### ARTISTS ###

  def get_artists(self):
    query = text('SELECT * FROM artists')
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output


  def get_artist_info(self, artist_id):
    query = text('SELECT name, birth_year, death_year FROM artists WHERE id =' + artist_id)
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output[0]


  def get_exhibits_for_artist (self, artist_id):
    query = text('SELECT e.name AS exhibit, type, creation_year FROM exhibits e JOIN artists_exhibits ae JOIN artists a ON e.id = ae.id_exhibit AND a.id = ae.id_artist WHERE ae.id_artist =' + artist_id)
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output


  def get_country_for_artist (self, artist_id):
    query = text('SELECT c.name from countries c JOIN artists_countries ac JOIN artists a ON  c.id = ac.id_country AND a.id = ac.id_artist where ac.id_artist =' + artist_id)
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    print(output)

    return output[0] if output != [] else ''


  def add_artist(self, name, birth_year, death_year):
    query = text('INSERT INTO artists VALUES (NULL, "' + str(name) + '", "' + str(birth_year) + '", "' + str(death_year) + '")')
    query_result = self.engine.execute(query)


  def remove_artist(self, name):
    query = text('DELETE FROM artists WHERE name = "' + name + '"')
    query_result = self.engine.execute(query)


  def add_exhibit_to_artist(self, artist_name, exhibit_name):
    query = text('INSERT INTO artists_exhibits VALUES ((SELECT id FROM artists WHERE name = "' + str(artist_name) + '"), (SELECT id FROM exhibits WHERE name = "' + str(exhibit_name) + '"))')
    query_result = self.engine.execute(query)


  def remove_exhibit_from_artist(self, exhibit_name, artist_id):
    query = text('DELETE FROM artists_exhibits WHERE id_exhibit = (SELECT id FROM exhibits WHERE name = "' + str(exhibit_name) + '") AND id_artist = "' + str(artist_id) + '"')
    query_result = self.engine.execute(query)


  ### COUNTRIES ###

  def countries(self):
    query = text('SELECT * FROM countries')
    query_result = self.engine.execute(query)

    output = []
    for row in query_result:
      output.append(dict(row))

    return output


  def add_country(self, country_name):
    query = text('INSERT INTO countries VALUES (NULL, "' + str(country_name) + '")')
    query_result = self.engine.execute(query)


  def remove_country(self, country_name):
    query = text('DELETE FROM countries WHERE name = "' + str(country_name) + '"')
    query_result = self.engine.execute(query)

  
  def add_artist_to_country(self, artist_id, country_name):
    query = text('INSERT INTO artists_countries VALUES ("' + str(artist_id) + '", (SELECT id FROM countries WHERE name = "' + str(country_name) + '"))')
    query_result = self.engine.execute(query)


  def remove_artist_from_country(self, artist_id):
    query = text('DELETE FROM artists_countries WHERE id_artist = "' + artist_id + '"')
    query_result = self.engine.execute(query)

    

# DB = DB()
# print(DB.get_museums())
