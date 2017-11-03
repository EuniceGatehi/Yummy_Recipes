""" app/__init__.py """

from flask import Flask
from app.userclass import User
from app.recipecategories import CategoryClass
from app.recipes import RecipesClass


# Initialize the app
app = Flask(
    __name__, instance_relative_config=True)
app.secret_key = 'lif3isgood'
user_object = User()
category_object = CategoryClass()
recipes_object = RecipesClass()
from app import views

# Load the config file
app.config.from_object('config')
