from flask import render_template, redirect, url_for,flash,request
from flask_login import login_required, current_user, login_user,logout_user
from ..models import Users
from .forms import Loginform,Signupform


from . import auth


@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = Signupform()
    if form.validate_on_submit():
        users = Users(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(users)
        db.session.commit()
        flash(f'account created for{form.username.data}')
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)



@auth.route('/login', methods=['GET','POST'])
def login():
    login = Loginform()
    if login.validate_on_submit():
        users = Users.query.filter_by(email = login.email.data).first()
        if users is not None and users.verify_password(login.password.data):
            login(users,login.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or Password')

    title = "Blog It login"
    return render_template('auth/login.html',login = login,title=title)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("main/index.html")