from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from ..models import Post,Users
from . import main

@main.route("/")
def home():
    title = 'hello'
    return render_template('index.html',title=title)

@main.route("/posts", methods = ['GET','POST'])
@login_required
def new_post():

    return render_template('/posts.html', title = true)


@main.route('/users/<usernam>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    return render_template("/profile/profile.html", users = users)