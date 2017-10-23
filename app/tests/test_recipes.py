"""test_recipes.py"""
import unittest
from app.recipes import Recipes


class TestCasesRecipes(unittest.TestCase):
    """
    Test for existence of recipe
    Test for special character in recipe name
    Test for correct output(recipe creation)

    """

    def setUp(self):
        """Setting up Recipe class
        """
        self.recipe = Recipe()

    def tearDown(self):
        """Removing Recipe class
        """
        del self.recipe

    def test_special_characters(self):
        """Check for special characters in recipe name
        """
        user = "eunicegatehi@gmail.com"
        msg = self.recipe.create_recipe("Ugali", user)
        self.assertEqual(msg, "No special characters (. , ! space [] )")


    def test_correct_output(self):
        """Check for correct recipe addition
        """
        msg = self.recipe.create_recipe(
            'Matoke', "eunicegatehi@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'eunicegatehi@gmail.com', 'name': 'Matoke'}])

    def test_edit_existing_recipe(self):
        """Check if edit name provided is similar to an existing recipe
        """
        self.recipe.create_recipe = [{'owner': 'eunice@gmail.com', 'name': 'Matoke'}, {
            'owner': 'eunicegatehi@gmail.com', 'name': 'Pilau Njeri'}]
        msg = self.recipes.create_recipe(
            'Pilau Njeri', 'Rice', "eunicegatehi@gmail.com")
        self.assertIn("name already exists", msg)


if __name__ == '__main__':
    unittest.main()