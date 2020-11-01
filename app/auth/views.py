from flask import render_template, redirect, url_for,flash
from flask_login import login_required, current_user

from . import main


@auth.route('/signup', methods=['GET','POST']):
def signup():
    def register():
        form = Signupform()
        if form.validate_on_submit():
            flash(f'account created for{form.username.data}')
            return redirect(url_for('main.home'))
        return render_template('signup.html' form=form)


@auth.route('/login', methods=['GET','POST']):
def login():
    def register():
        form = loginform()
        return render_template('login.html' form=form)