#Carblog/__init__.py
import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy  
from flask_migrate import Migrate 
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


##database set up##

basedir = os.path.abspath(os.path.dirname(__file__)) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app,db) 


###
##login config
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from Carblog.core.views import core 
from Carblog.users.views import users 
from Carblog.blog_posts.views import blog_posts 
from Carblog.error_pages.handlers import error_pages

from Carblog.blog_posts.views import blog_posts
from Carblog.blog_posts.api import blog_posts_api

app.register_blueprint(blog_posts_api, url_prefix='/api/posts')


app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
