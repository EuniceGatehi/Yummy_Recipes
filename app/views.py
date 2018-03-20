""" views.py """
from functools import wraps
from flask import render_template, request, session, redirect
from app import app, user_object, category_object, recipes_object

# Variable stores user's email
user = None

def authorize(f):
    """Function to authenticate users when accessing other pages"""
    @wraps(f)
    def check(*args, **kwargs):
        """Function to check login status"""
        if "email" in session:
            return f(*args, **kwargs)
        response_message = "Please login"
        return render_template("login.html", resp=response_message)
    return check


@app.route('/')
def index():
    """Handles rendering of index page
    """
    return render_template("index.html")


@app.route('/registration', methods=['GET', 'POST'])
def register():
    """Handles registration of users
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirm-password']

        response_message = user_object.registeruser(username, email, password, confirmpassword)
        if response_message == "Successfully registered. You can now login!":
            return render_template("login.html", resp=response_message)
        return render_template("registration.html", error=response_message)

    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response_message = user_object.login(email, password)
        if response_message == "Successfully logged in, create recipecategory!":
            session['email'] = email
            global user
            user = email
            user_categories = category_object.get_owner(user)
            return render_template('recipecategory.html', resp=response_message, recipecategory=user_categories)
        return render_template('login.html', error=response_message)
    return render_template("login.html")

@app.route('/recipecategory', methods=['GET', 'POST'])
@authorize
def recipecategory():
    """Handles recipecategory creation
    """
    if user == session['email']:
        global user_categories
        user_categories = category_object.get_owner(user)
    if request.method == 'POST':
        category_name = request.form['category-name']
        response_message = category_object.create_category(category_name, user)
        user_categories = category_object.get_owner(user)
        if isinstance(response_message, list):
            return render_template('recipecategory.html', recipecategory=response_message)
        return render_template('recipecategory.html', error=response_message, recipecategory=user_categories)
    return render_template('recipecategory.html', recipecategory=category_object.get_owner(user))

@app.route('/edit-category', methods=['GET', 'POST'])
@authorize
def save_edits():
    """ Handles editing of categories """
    if user == session['email']:
        user_categories = category_object.get_owner(user=user)
    if request.method == 'POST':
        edit_name = request.form['category_name']
        original_name = request.form['category_name_org']
        response_message = category_object.edit_category(edit_name, original_name, user)
        user_categories = category_object.get_owner(user=user)
        if response_message == category_object.recipe_category:
            return redirect('/recipecategory')
        #existing = category_object.recipe_category
        return render_template('recipecategory.html', error=response_message, recipecategory=user_categories)
    return render_template('recipecategory.html')


@app.route('/delete-category', methods=['GET', 'POST'])
@authorize
def delete_recipecategory():
    """Handles deletion of recipecategory and its items
    """
    if request.method == 'POST':
        delete_name = request.form['category_name']
        response_message = category_object.delete_category(delete_name, user=user)
        # Delete its recipes
        recipes_object.deleted_category_recipes(delete_name)
        return redirect('/recipecategory')
        response = "Successfuly deleted" + delete_name
        return render_template('recipecategory.html', resp=response, recipecategory=response_message)


@app.route('/recipes/<recipecategory>', methods=['GET', 'POST'])
@authorize
def recipes(recipecategory):
    """Handles recipes creation
    """
    # Get a list of users recipes for a specific recipe category
    user_recipes = recipes_object.owner_recipes(user, recipecategory)
    # specific recipe category
    new_category = [item['name']
    for item in user_recipes if item['category'] == recipecategory]
    if request.method == 'POST':
        recipe_name = request.form['recipe-name']
        recipe_description = request.form['recipe-description']
        response_message = recipes_object.add_recipe(recipecategory, recipe_name,recipe_description, user)
        if isinstance(response_message, list):
            new_category = [item['name']
                        for item in response_message if item['category'] == recipecategory]
            return render_template("recipes.html", recipecategory=new_category, name=recipecategory)
        # response_message is not a list
        return render_template("recipes.html", error=response_message, name=recipecategory, recipecategory=new_category)
    else:
        res = "You can now add your recipes"
        return render_template('recipes.html', resp=res, name=recipecategory, recipecategory=new_category)


@app.route('/edit-recipe', methods=['GET', 'POST'])
@authorize
def edit_recipe():
    """ Handles editing of recipes
    """
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        recipe_name_org = request.form['recipe_name_org']
        category_name = request.form['category_name']
        response_message = recipes_object.edit_recipe(
            recipe_name, recipe_name_org, category_name, user)
        if isinstance(response_message, list):
            res = "Successfully edited recipe " + recipe_name_org
            # Get edited list of the current recipe category
            newcategory = [item['name']
                       for item in response_message if item['category'] == category_name]
            return render_template("recipes.html", recipecategory=newcategory, name=category_name, resp=res)
        else:
            # Get user's recipes in the current recipe category
            user_recipes = recipes_object.owner_recipes(user, category_name)
            new_category = [item['name']
                        for recipe in user_recipes if recipe['category'] == category_name]
    return render_template("recipes.html", recipecategory=new_category, name=category_name, error=response_message)

        

@app.route('/delete-recipe', methods=['GET', 'POST'])
@authorize
def delete_recipe():
    """ Handles deletion of recipes
    """
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']

        category_name = request.form['category_name']
        response_message = recipes_object.delete_recipe(recipe_name, user, category_name)
        response = "Successfuly deleted recipe " + recipe_name
        return render_template("recipes.html", recipecategory=response_message, name=category_name, resp=response)


@app.route('/logout')
@authorize
def logout():
    """Handles logging out of users"""
    session.pop('email', None)
    return render_template("login.html")
