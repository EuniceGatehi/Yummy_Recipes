""" app/__init__.py """

from flask import Flask
from app.userclass import User
from app.recipecategories import RecipecategoryClass
from app.recipes import RecipesClass


# Initialize the app
app = Flask(
    __name__, instance_relative_config=True)
app.secret_key = 'lif3isgood'
user_obj = User()
recipecategory_obj = RecipecategoryClass()
reciperecipes_obj = RecipesClass()
from app import views

# Load the config file
app.config.from_object('config')
