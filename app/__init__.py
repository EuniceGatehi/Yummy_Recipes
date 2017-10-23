# app/__init__.py

from flask import Flask
from app.userclass import User
from app.recipes import Recipes
from app.userclass import User 
# Initialize the app
app = Flask(__name__, instance_relative_config=True)
user= User()
recipes= Recipes()

# Load the views
from app import views

# Load the config file
app.config.from_object('config')