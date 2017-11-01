"""recipes.py"""
import re


class RecipesClass(object):
    """Handles creation,editing and deletion of recipes
    """

    def __init__(self):
        # list to hold recipes within a recipe category
        self.recipe_category = []

    def owner_recipes(self, user, recipe_name):
        """Returns recipes belonging to a user
        Args
             user
        returns
            list of user's recipes
        """
        user_recipes = [item for item in self.recipe_category if item['owner']
                      == user and item['category'] == recipe_name]
        return user_recipes

    def add_recipe(self, category_name, recipe_name, user):
        """Handles adding a recipe to a recipe category
            Args
                recipe category name
            result
                list of recipes
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9 _]*$", recipe_name):
            # Get users recipes
            my_recipes = self.owner_recipes(user, category_name)
            for item in my_recipes:
                if item['name'] == recipe_name:
                    return "recipe name already exists"
            activity_dict = {
                'name': recipe_name,
                'category': category_name,
                'owner': user
            }
            self.recipe_category.append(activity_dict)
            return self.owner_recipes(user, category_name)
        return "No special characters (. , ! [] )"

    def edit_recipe(self, recipe_name, org_recipe_name, category_name, user):
        """Handles editing of recipes
            Args
                editted name and original name
            returns
                error message or a list of recipes
        """
        # Get users recipes
        my_recipes = self.owner_recipes(user, category_name)
        for item in my_recipes:
            if item['category'] == category_name:
                if item['name'] != recipe_name:
                    if item['name'] == org_recipe_name:
                        del item['name']
                        edit_dict = {
                            'name': recipe_name,
                        }
                        item.update(edit_dict)
                else:
                    return "Recipe name already exists"
        return self.owner_recipes(user, category_name)

    def delete_recipe(self, recipe_name, user, category_name):
        """Handles deletion of recipe category recipes
       
        """
        # Get users 
        for item in range(len(self.recipe_category)):
            if self.recipe_category[item]['name'] == recipe_name:
                del self.recipe_category[item]
                break
        deleted_recipe_category = []
        my_recipes = self.owner_recipes(user, category_name)
        for recipe_s in my_recipes:
            deleted_recipe_category.append(recipe_s['name'])
        return deleted_recipe_category

    def deleted_category_recipes(self, category_name):
        """Delete recipes for the category that was deleted
        Args
           category name
        """
        self.recipe_category[:] = [
            item for recipe in self.recipe_category if recipe.get('category') != category_name]
