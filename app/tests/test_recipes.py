"""test_recipes.py"""
import unittest
from app.recipes import RecipesClass


class TestCasesRecipes(unittest.TestCase):
    """
    Test for existence of recipe in recipe creation
    Test for special character in recipe names
    Test for correct owner
    Test for correct output(recipes creation)
    Test for deletion of existing recipe
    Test for editing recipe names
    Test for editing recipe names with existing recipe names
    Test for deletion of recipe 
    """

    def setUp(self):
        """Setting up Recipesclass
        """
        self.recipes_class_obj = RecipesClass()

    def tearDown(self):
        """Removing Recipesclass
        """
        del self.recipes_class_obj

    def test_existing_recipe(self):
        """Check to see recipe name exists or not
         """
        self.recipes_class_obj.recipe_category = \
            [{'owner': 'mary@gmail.com', 'category': 'Breakfast', 'name': 'Bread'}, {
                'owner': 'mary@gmail.com', 'category': 'Lunch', 'name': 'matoke'}]
        msg = self.recipes_class_obj.add_recipe(
            "Breakfast", "Bread", "mary@gmail.com")
        self.assertIn("recipe name already exists", msg)

    def test_special_characters_name(self):
        """Check for special characters in recipe name
        """
        msg = self.recipes_class_obj.add_recipe(
            "Breakfast", "Bread!", "mary@gmail.com")
        self.assertIn("No special characters (. , ! [] )", msg)

    def test_owner(self):
        """ Check for recipes belonging to owner"""
        self.recipes_class_obj.recipe_category = \
            [{'owner': 'mary@gmail.com', 'category': 'Breakfast', 'name': 'Bread'},
             {'owner': 'wanjigi@gmail.com',
              'category': 'Breakfast', 'name': 'Blueband'},
             {'owner': 'mary@gmail.com', 'category': 'Breakfast', 'name': 'Blueband'}]
        user = "wanjigi@gmail.com"
        recipecategory = "Breakfast"
        msg = self.recipes_class_obj.owner_recipes(user, recipecategory)
        self.assertEqual(
            msg, [{'owner': 'wanjigi@gmail.com', 'category': 'Breakfast', 'name': 'Blueband'}])

    def test_correct_output_recipe(self):
        """Check for correct recipe creation
        """
        msg = self.recipes_class_obj.add_recipe(
            "Breakfast", "Bread", "mary@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'mary@gmail.com', 'category': 'Breakfast', 'name': 'Bread'}])

    def test_editing_recipe(self):
        """Check for edits to recipename
        """
        self.recipes_class_obj.recipe_category = \
        [{'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Snacks'}, {
            'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Matoke'}]
        msg = self.recipes_class_obj.edit_recipe(
            'Soda', 'Matoke', 'Dinner', "mary@gmail.com")
        self.assertEqual(msg, \
        [{'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Snacks'}, {
            'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Soda'}])

    def test_edit_existing_recipename(self):
        """Check if edit name provided is similar to an existing recipe
        """
        self.recipes_class_obj.recipe_category = \
        [{'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Snacks'}, {
            'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Matoke'}]
        msg = self.recipes_class_obj.edit_recipe(
            'Snacks', 'Matoke', 'Dinner', "mary@gmail.com")
        self.assertIn("Recipe name already exists", msg)

    def test_delete_recipe(self):
        """Check to see if recipe is deleted
        """
        self.recipes_class_obj.recipe_category = \
        [{'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Snacks'}, {
            'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Matoke'}]
        msg = self.recipes_class_obj.delete_recipe(
            'Matoke', "mary@gmail.com", 'Dinner')
        self.assertEqual(msg, ['Snacks'])

    def test_deleted_category(self):
        """Check if categpry deleted will have its recipes deleted too
        """
        self.recipes_class_obj.recipe_category = \
        [{'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Snacks'}, {
            'owner': 'mary@gmail.com', 'category': 'Dinner', 'name': 'Matoke'}]
        res = self.recipes_class_obj.deleted_category_recipes('Dinner')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()
