from datetime import datetime
from flask_login import LoginManager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from .import login_manager

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))



class Users(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique = True, nullable=False)
    email = db.Column(db.String(255), unique = True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False, default = 'image.jpg')
    bio = db.Column(db.String(255))
    posts = db.relationship('Post', backref='author', lazy=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f"Users('{self.username}','{self.email}','{self.photo}')"


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

    def __repr__(self):
        return f"Post('{self.title}','{self.date}')"


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('Users',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'Users {self.name}'
