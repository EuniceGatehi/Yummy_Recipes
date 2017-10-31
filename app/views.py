""" views.py """
from functools import wraps
from flask import render_template, request, session
from app import app, user_obj, recipecategory_obj, reciperecipes_obj

# Variable stores user's email
user = None

def authorize(f):
    """Function to authenticate users when accessing other pages"""
    @wraps(f)
    def check(*args, **kwargs):
        """Function to check login status"""
        if "email" in session:
            return f(*args, **kwargs)
        msg = "Please login"
        return render_template("login.html", resp=msg)
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
        cpassword = request.form['confirm-password']

        msg = user_obj.registeruser(username, email, password, cpassword)
        if msg == "Successfully registered. You can now login!":
            return render_template("login.html", resp=msg)
        return render_template("registration.html", error=msg)

    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        msg = user_obj.login(email, password)
        if msg == "Successfully logged in, create recipecategory!":
            session['email'] = email
            global user
            user = email
            user_categories = recipecategory_obj.get_owner(user)
            return render_template('recipecategory.html', resp=msg, recipecategory=user_categories)
        return render_template('login.html', error=msg)
    return render_template("login.html")

@app.route('/recipecategory', methods=['GET', 'POST'])
@authorize
def recipecategory():
    """Handles recipecategory creation
    """
    if user == session['email']:
        global user_categories
        user_categories = recipecategory_obj.get_owner(user)
    if request.method == 'POST':
        category_name = request.form['category-name']
        msg = recipecategory_obj.create_category(category_name, user)
        user_categories = recipecategory_obj.get_owner(user)
        if isinstance(msg, list):
            return render_template('recipecategory.html', recipecategory=msg)
        return render_template('recipecategory.html', error=msg, recipecategory=user_categories)
    return render_template('recipecategory.html', recipecategory=recipecategory_obj.get_owner(user))

@app.route('/edit-category', methods=['GET', 'POST'])
@authorize
def save_edits():
    """ Handles editing of categories """
    if user == session['email']:
        user_categories = recipecategory_obj.get_owner(user=user)
    if request.method == 'POST':
        edit_name = request.form['category_name']
        org_name = request.form['category_name_org']
        msg = recipecategory_obj.edit_category(edit_name, org_name, user)
        user_categories = recipecategory_obj.get_owner(user=user)
        if msg == recipecategory_obj.recipe_category:
            response = "Successfully edited category " + org_name
            return render_template('recipecategory.html', resp=response, recipecategory=msg)
        #existing = recipecategory_obj.recipe_category
        return render_template('recipecategory.html', error=msg, recipecategory=user_recipes)
    return render_template('recipecategory.html')


@app.route('/delete-category', methods=['GET', 'POST'])
@authorize
def delete_recipecategory():
    """Handles deletion of recipecategory and its items
    """
    if request.method == 'POST':
        del_name = request.form['category_name']
        msg = recipecategory_obj.delete_category(del_name, user=user)
        # Delete its recipes
        reciperecipes_obj.deleted_category_recipes(del_name)
        response = "Successfuly deleted" + del_name
        return render_template('recipecategory.html', resp=response, recipecategory=msg)


@app.route('/recipes/<recipecategory>', methods=['GET', 'POST'])
@authorize
def recipes(recipecategory):
    """Handles recipes creation
    """
    # Get a list of users recipes for a specific recipe category
    user_recipes = reciperecipes_obj.owner_recipes(user, recipecategory)
    # specific recipe category
    new_category = [item['name']
                for item in user_recipes if item['category'] == recipecategory]
    if request.method == 'POST':
        recipe_name = request.form['recipe-name']
        msg = reciperecipes_obj.add_recipe(recipecategory, recipe_name, user)
        if isinstance(msg, list):
            new_category = [item['name']
                        for item in msg if item['category'] == recipecategory]
            return render_template("recipes.html", recipecategory=new_category, name=recipecategory)
        # msg is not a list
        return render_template("recipes.html", error=msg, name=recipecategory, recipecategory=new_category)
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
        msg = reciperecipes_obj.edit_recipe(
            recipe_name, recipe_name_org, category_name, user)
        if isinstance(msg, list):
            res = "Successfully edited recipe " + recipe_name_org
            # Get edited list of the current recipe category
            newcategory = [item['name']
                       for item in msg if item['category'] == category_name]
            return render_template("recipes.html", recipecategory=newcategory, name=category_name, resp=res)
        else:
            # Get user's recipes in the current recipe category
            user_recipes = reciperecipes_obj.owner_recipes(user, category_name)
            new_category = [item['name']
                        for item in user_recipes if recipe['category'] == category_name]
    return render_template("recipes.html", recipecategory=new_category, name=category_name, error=msg)

        

@app.route('/delete-recipe', methods=['GET', 'POST'])
@authorize
def delete_recipe():
    """ Handles deletion of recipes
    """
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        category_name = request.form['category_name']
        msg = reciperecipes_obj.delete_recipe(recipe_name, user, category_name)
        response = "Successfuly deleted recipe " + recipe_name
        return render_template("recipes.html", recipecategory=msg, name=category_name, resp=response)


@app.route('/logout')
@authorize
def logout():
    """Handles logging out of users"""
    session.pop('email', None)
    return render_template("login.html")
