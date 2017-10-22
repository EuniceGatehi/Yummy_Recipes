# views.py

from flask import render_template,request,session

from app import app, user, recipes

user_loggedin = None 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['inputEmail']
        password=request.form['inputPassword']
        result = user.userlogin(email,password)
        
        if result == "log in successful":
            global user_loggedin
            user_loggedin = email
            return render_template("recipes.html")
        
        return render_template("login.html",resp = result)

    return render_template("login.html")

@app.route('/registration',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username=request.form['inputName']
        email=request.form['inputEmail']
        password=request.form['inputPassword']
        cpassword=request.form['inputConfirmPassword']
        result = user.registeruser(username,email,password,cpassword)
        if result == "Registration successful please proceed with log in":
            return render_template("login.html",resp=result)
        return render_template("registration.html",resp=result)
    return render_template("registration.html")        


@app.route('/recipes',methods=['GET','POST'])
def recipe():
    print (user_loggedin)
    # user_recipe= recipes.get_owner(user_loggedin)      
    if request.method == 'POST':
        recipename=request.form['inputrecipename']
        result = recipes.create_recipe(recipename,user_loggedin)
        if isinstance(result, list):
            return render_template("recipes.html", recipes=result)  
        return render_template("recipes.html",error=result, recipes=user_recipe)
    return render_template("recipes.html")
