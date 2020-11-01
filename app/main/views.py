from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from . import main

@main.route("/")
def home():
    title = 'hello'
    return render_template('index.html',title=title)