from datetime import datetime

from flask import (Flask, abort, flash, redirect, render_template, request,
url_for)

from flask.ext.stormpath import(StormpathError, StormpathManager, User,
login_required, login_user, logout_user, user)

app=Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY']='secretkey'
app.config['STORMPATH_API_KEY_FILE']= 'apiKey.properties'
app.config['STORMPATH_APPLICATION'] = 'FunBlogr'

stormpath_manager = StormpathManager(app)

@app.route('/')
def show_posts():
  posts = []




if __name__ == '__main__':
  app.run(host='0.0.0.0')
