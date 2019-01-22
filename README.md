[![Build Status](https://travis-ci.org/EuniceGatehi/Yummy_Recipes.svg?branch=developchallengetwo)](https://travis-ci.org/EuniceGatehi/Yummy_Recipes)
[![Coverage Status](https://coveralls.io/repos/github/EuniceGatehi/Yummy_Recipes/badge.svg?branch=developchallengetwo)](https://coveralls.io/github/EuniceGatehi/Yummy_Recipes?branch=developchallengetwo)

# Yummy_Recipes
Product Challenge 1

This application helps users in the management of recipes and categories. It helps users create,update and delete their categories as well as add their favorite recipes to these categories.

Yummy Recipes helps users create accounts so they can log in, create, view and delete recipes.

Follow this link to interact with the working verion of the app https://yummyflask.herokuapp.com
    # Prerequisites

    You will need python 3.6.3 or a later python version.

    # installation
    clone the repository 

    FOR HTTPS
    https://github.com/EuniceGatehi/Yummy_Recipes.git

    FOR SSH 

    git@github.com:EuniceGatehi/Yummy_Recipes.git

    In your project folder, create a virtual environment

    ```$ virtualenv envname```

    Activate the virtual environment you have just created

    ```$ source envname/bin/activate```

    Install the application's dependencies from requirements.txt to the virtual environment

    ```$ (envname) pip install -r requirements.txt```

    Set up Unit Test Environment (I used nosetest)

    *run the following command to install nose unit testing environment:

    ```$  (envname) pip install nose```
    *this is how you run your tests:
        *in browser :noestests
        *in editor or comandline :  nosetests --with-coverage --cover-package=tests && coverage report

    ##Running the program

    Run the program by typing the command in your terminal : 

    ```$  (envname) python run.py```

    and voila!you can now use the application.
