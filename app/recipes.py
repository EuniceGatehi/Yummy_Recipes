import re
class Recipes(object):

    """
    Handles creation of recipes
    """
    def __init__(self):
        #list to hold recipes as a user creates
        self.recipes_list=[]
    def get_owner(self,user):

        #returns recipes belonging to user
        user_recipes_list=[
            item for item in self.recipes_list if item['owner'] == user]
        return user_recipes_list
    def create_recipe(self,recipe,user):
        #creation of recipes
        if re.match("^[a-zA-Z0-9 _]*$", recipe):
            my_recipes_list=self.get_owner(user)
            for item in my_recipes_list:
                if recipe == item['name']:
                    return"recipe name already exists"
            recipe_dict = {
                'name':recipe,
                'owner':user,
            }
            self.recipes_list.append(recipe_dict)
        else:
            return"No special characters(. , ! space [])"
        return self.get_owner(user)

        
    
        
