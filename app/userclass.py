import re
class User(object):
    """
    Class to handle registration of users
    """
    def __init__(self):
        #list to contain users
        self.user_list=[]

    def registeruser(self,username,email,password,cpassword):
        #empty dic to hold each user
        user_dict = {}
        #check for existing user
        for user in self.user_list:
            if email == user['email']:
                return"User already exists"
        #check for password length and mismatch
        if len(password) < 6:
            return "your password should atleast be 6 characters long"
        elif not re.match("^[a-zA-Z 0-9]*$",username):
            return  "no special characters"
        #regular expression for email
        elif not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)", email):
            return "please provide a valid email address"
        elif password==cpassword:
            user_dict['username']=username
            user_dict['email']=email
            user_dict['password']=password
            self.user_list.append(user_dict)
            
        else:
            return "password mismatch"
        return "Registration successful please proceed with log in"

    def userlogin(self,email,password):
        for user in self.user_list:
            if email == user['email']:
                if password == user['password']:
                    return "log in successful"
                return "password mismatch"
        return "you are not registered. please sign up"