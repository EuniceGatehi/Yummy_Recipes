""" userclass.py """
import re


class User(object):
    """
    Class to handle registration and loggin of users
    """

    def __init__(self):
        # list to contain users
        self.user_list = []

    def registeruser(self, username, email, password, confirmpassword):
        """
        Args
            username(string):name
            email(string):user email
            upasswd(string):password
        Return
           error response_message or success response_message
        Purpose
           register users that have signed up by adding to dictionary
        """
        # empty dict to hold each user
        user_details = {}
        # check for existing user
        for user in self.user_list:
            if email == user['email']:
                return "User already exists. Please login"
        # check for password length and mismatch
        if len(password) < 6:
            return "Your password should be at least 6 characters long"
        elif not re.match("^[a-zA-Z0-9_]*$", username):
            return "No special characters (. , ! space [] )"
        # regular expression for email
        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            return "Please provide a valid email address"
        elif password == confirmpassword:
            user_details['username'] = username
            user_details['email'] = email
            user_details['password'] = password
            self.user_list.append(user_details)
        else:
            return "Password mismatch"
        return "Successfully registered. You can now login!"

    def login(self, email, password):
        """
        Args
            email(string):user email
            userpassword(string):password
        Return
           error response_message or success response_message
        Purpose
           Login users
        """
        for user in self.user_list:
            if email == user['email']:
                if password == user['password']:
                    return "Successfully logged in, create recipecategory!"
                return "Password mismatch"
        return "You have no account,please sign up"
