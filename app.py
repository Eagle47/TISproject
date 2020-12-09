from flask import Flask, request, render_template
from db import DB

app = Flask(__name__)
app.config['DEBUG'] = True
DB = DB()


### MUSEUMS ###

@app.route('/')
def main_page():
  return render_template('main_page.html')


@app.route('/museums')
def museums():
  museums = DB.get_museums()

  return render_template('museums.html', museums=museums)


@app.route('/museums/<museum_id>')
def museum(museum_id):
  museum_data = DB.get_museum_info(museum_id)
  exhibits_data = DB.get_exhibits_for_museum(museum_id)

  return render_template('museum.html', museum=museum_data, exhibits=exhibits_data)


@app.route('/museums/add', methods=['GET', 'POST'])
def add_museum():
  if request.method == 'POST':
    name = request.form.get('name')
    foundation_year = request.form.get('foundation_year')
    city = request.form.get('city')
    DB.add_museum(name, foundation_year, city)
  
  return render_template('add_museum.html')


@app.route('/museums/remove', methods=['GET', 'POST'])
def remove_museum():
  if request.method == 'POST':
    name = request.form.get('name')
    DB.remove_museum(name)

  return render_template('remove_museum.html')


@app.route('/museums/add_exhibit', methods=['GET', 'POST'])
def add_exhibit_to_museum():
  if request.method == 'POST':
    museum_name = request.form.get('museum_name')
    exhibit_name = request.form.get('exhibit_name')
    DB.add_exhibit_to_museum(museum_name, exhibit_name)

  return render_template('add_exhibit_to_museum.html')


@app.route('/museums/remove_exhibit', methods=['GET', 'POST'])
def remove_exhibit_from_museum():
  if request.method == 'POST':
    exhibit_name = request.form.get('exhibit_name')
    DB.remove_exhibit_from_museum(exhibit_name)

  return render_template('remove_exhibit_from_museum.html')



### EXHIBITS ###

@app.route('/exhibits')
def exhibits():
  exhibits = DB.get_exhibits()

  return render_template('exhibits.html', exhibits=exhibits)


@app.route('/exhibits/add', methods=['GET', 'POST'])
def add_exhibit():
  if request.method == 'POST':
    name = request.form.get('name')
    typ = request.form.get('typ')
    creation_year = request.form.get('creation_year')
    DB.add_exhibit(name, typ, creation_year)

  return render_template('add_exhibit.html')


@app.route('/exhibits/remove', methods=['GET', 'POST'])
def remove_exhibit():
  if request.method == 'POST':
    name = request.form.get('name')
    DB.remove_exhibit(name)

  return render_template('remove_exhibit.html')


### ARTISTS ###

@app.route('/artists')
def artists():
  artists = DB.get_artists()

  return render_template('artists.html', artists=artists)


@app.route('/artists/<artist_id>')
def artist(artist_id):
  artist_data = DB.get_artist_info(artist_id)
  exhibits_data = DB.get_exhibits_for_artist(artist_id)
  country_data = DB.get_country_for_artist(artist_id)

  return render_template('artist.html', artist=artist_data, exhibits=exhibits_data, country=country_data, artist_id=artist_id)


@app.route('/artists/add', methods=['GET', 'POST'])
def add_artist():
  if request.method == 'POST':
    name = request.form.get('name')
    birth_year = request.form.get('birth_year')
    death_year = request.form.get('death_year')
    DB.add_artist(name, birth_year, death_year)

  return render_template('add_artist.html')


@app.route('/artists/remove', methods=['GET', 'POST'])
def remove_artist():
  if request.method == 'POST':
    name = request.form.get('name')
    DB.remove_artist(name)

  return render_template('remove_artist.html')


@app.route('/artists/add_exhibit', methods=['GET', 'POST'])
def add_exhibit_to_artist():
  if request.method == 'POST':
    artist_name = request.form.get('artist_name')
    exhibit_name = request.form.get('exhibit_name')
    DB.add_exhibit_to_artist(artist_name, exhibit_name)

  return render_template('add_exhibit_to_artist.html')


@app.route('/artists/<artist_id>/remove_exhibit', methods=['GET', 'POST'])
def remove_exhibit_from_artist(artist_id):
  if request.method == 'POST':
    exhibit_name = request.form.get('exhibit_name')
    DB.remove_exhibit_from_artist(exhibit_name, artist_id)

  return render_template('remove_exhibit_from_artist.html', artist_id=artist_id)


### COUNTRIES ###

@app.route('/artists/add_country', methods=['GET', 'POST'])
def add_country():
  if request.method == 'POST':
    country_name = request.form.get('country_name')
    DB.add_country(country_name)

  countries = DB.countries()

  return render_template('add_country.html', countries=countries)


@app.route('/artists/remove_country', methods=['GET', 'POST'])
def remove_country():
  if request.method == 'POST':
    country_name = request.form.get('country_name')
    DB.remove_country(country_name)

  countries = DB.countries()

  return render_template('remove_country.html', countries=countries)


@app.route('/artists/<artist_id>/add_to_country', methods=['GET', 'POST'])
def add_artist_to_country(artist_id):
  if request.method == 'POST':
    country_name = request.form.get('country_name')
    DB.add_artist_to_country(artist_id, country_name)

  return render_template('add_to_country.html')


@app.route('/artists/<artist_id>/remove_from_country', methods=['GET', 'POST'])
def remove_artist_from_country(artist_id):
  if request.method == 'POST':
    DB.remove_artist_from_country(artist_id)

  return render_template('remove_from_country.html')



app.run(host='0.0.0.0', port=5005)
