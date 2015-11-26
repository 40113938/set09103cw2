from flask import Flask, request, render_template, g, url_for
import sqlite3
app = Flask(__name__)

def get_db():
  return sqlite3.connect('film.db')

@app.route("/welcome/", methods=['POST', 'GET'])
def welcome():
    return render_template('welcome.html')

@app.route("/films/", methods=['POST', 'GET'])
def films():
  band = request.args.get('q', '')
  g.db = get_db()
  if band == '':
    cur = g.db.execute ('SELECT * from film ORDER BY name')
  else:
    cur = g.db.execute ('SELECT * from film where name = ?', (band, ))
  film = [dict(name=row[0],
  yoc=row[1], main_actor=row[2], genre=row[3]) for row in cur.fetchall()]
  return render_template('films.html', band=band, film=film)

@app.route("/actors/", methods=['POST', 'GET'])
def actors():
  band = request.args.get('q', '')
  g.db = get_db()
  if band == '':
    cur = g.db.execute ('SELECT * FROM actor  ORDER BY name')
  else:
    cur.g.db.execute ('SELECT * FROM actor  where name = ?', (band, ))
  actor = [dict(name=row[0],
  age=row[1], known_for=row[2], nationality=row[3]) for row in cur.fetchall()]
  return render_template('actors.html', band=band, actor=actor)

@app.route("/search/", methods=['POST', 'GET'])
def search():
  searchm = request.args.get('key', '')
  g.db = get_db()
  if searchm  == '':
    cur = g.db.execute ("SELECT * FROM film")
  else:
    cur = g.db.execute ("SELECT * FROM film  WHERE name like ?", ("%" +  searchm  + "%", ))
  name = [dict(name=row[0], yoc=row[1], main_actor=row[2], genre=row[3])for row in cur.fetchall()]
  return render_template('search.html', searchm=searchm, name=name)

@app.route("/add/", methods=['POST', 'GET'])
def add():
  return render_template('add.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
