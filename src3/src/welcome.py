from flask import Flask, request, render_template, g, url_for
import sqlite3
app = Flask(__name__)
app.secret_key = 'secret'

valid_email = 'richard@hotmail.co.uk'
validpwhash = bcrypt.hashpw('secretpass', bcrypt.gensalt())

def check_auth(email, password):
  if(email == valid_email and valid_pwhash ==
  bcrypt.hashpw(password.encode('utf-8'),valid_pwhash)):
    return True
  return False

def requires_login(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    status = session.get('logged_in', False)
    if not status:
      return redirect(url_for('.root'))
    return f(*args, **kwargs)
  return decorated

@app.route('/logout/')
def logout():
  session['logged_in'] = False
  return redirect(url_for('.root'))

@app.route("/secret/")
@requires_login
def secret():
  return "Secret Page"


def get_db():
  return sqlite3.connect('music.db')

@app.route("/welcome/", methods=['POST', 'GET'])
def welcome():
  if request.method == 'POST':
    print request.form
    print "its all over richard"
    search = request.form['search']
    return "You searched for %s" % search
  else:
    return render_template('welcome.html')

@app.route("/login/", methods=['POST','GET'])
def login():
  return render_template('login.html')

@app.route("/artist/", methods=['POST', 'GET'])
def artist():
  band = request.args.get('q', '')
  g.db = get_db()
  if band == '':
    cur = g.db.execute ('SELECT * from artist ORDER BY name')
  else:
    cur = g.db.execute ('SELECT * from artist where name = ?', (band, ))
  artist = [dict(name=row[0],
  yoc=row[1], nationality=row[2], genre=row[3]) for row in cur.fetchall()]
  return render_template('artist.html', band=band, artist=artist)

@app.route("/album/", methods=['POST', 'GET'])
def album():
  band = request.args.get('q', '')
  g.db = get_db()
  if band == '':
    cur = g.db.execute ('SELECT * FROM album ORDER BY name')
  else:
    cur.g.db.execute ('SELECT * FROM album where name = ?', (band, ))
  album = [dict(name=row[0],
  artist=row[1], yor=row[2], length=row[3]) for row in cur.fetchall()]
  return render_template('album.html', band=band, album=album)

@app.route("/search/", methods=['POST', 'GET'])
def search():
  searchm = request.args.get('key', '')
  g.db = get_db()
  if searchm  == '':
    cur = g.db.execute ("SELECT * FROM artist")
  else:
    cur = g.db.execute ("SELECT * FROM artist WHERE name like ?", ("%" +  searchm  + "%", ))
  name = [dict(name=row[0], yoc=row[1], nationality=row[2], genre=row[3])for row in cur.fetchall()]
  return render_template('search.html', searchm=searchm, name=name)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
