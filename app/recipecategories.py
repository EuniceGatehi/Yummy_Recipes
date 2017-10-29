""" recipecategories.py """
import re


class RecipecategoryClass(object):
    """
    Handles creation of recipe categories
    """

    def __init__(self):
        # list to hold recipe category a user creates
        self.recipe_category = []

    def get_owner(self, user):
        """Returns recipe categories belonging to a user
        Args
            user
        returns
            list of user's recipe categories
        """
        user_recipe_category = [
            item for item in self.recipe_category if item['owner'] == user]
        return user_recipe_category

    def create_category(self, category_name, user):
        """Handles creation of recipe categories
            Args
                category name
            result
                recipe categories
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9 _]*$", category_name):
            # Get users recipe categories
            my_recipe_categories = self.get_owner(user)
            # check if category name exists
            for item in my_recipe_categories:
                if category_name == item['name']:
                    return "recipe category name already exists."
            recipe_dict = {
                'name': category_name,
                'owner': user,
            }
            self.recipe_category.append(recipe_dict)
        else:
            return "No special characters (. , ! space [] )"
        return self.get_owner(user)

    def edit_category(self, edit_name, org_name, user):
        """Handles edits made to recipe category name
            Args
                editted name and original name
            returns
                error message or a list of recipe categories
        """
        if re.match("^[a-zA-Z0-9 _]*$", edit_name):
            # Get users categories
            my_recipe_categories = self.get_owner(user)
            for item in my_recipe_categories:
                if edit_name != item['name']:
                    if org_name == item['name']:
                        del item['name']
                        edit_dict = {
                            'name': edit_name,
                        }
                        item.update(edit_dict)
                else:
                    return "Recipe category name already exists"
        else:
            return "No special characters (. , ! space [] )"
        return self.get_owner(user)

    def delete_category(self, category_name, user):
        """Handles removal of category name using list comprehension
            Args
                 category name
            returns
                 list with name removed
        """
        # Delete recipe category with name = category_name
        for item in range(len(self.recipe_category)):
            if self.recipe_category[item]['name'] == category_name:
                del self.recipe_category[item]
                break
        # Get users recipe categories
        my_recipe_categories = self.get_owner(user)
        return my_recipe_categories
    