"""test_recipecategories.py"""
import unittest
from app.recipecategories import CategoryClass


class TestCasesRecipecategory(unittest.TestCase):
    """
    Test for existence of recipe category in recipe category creation
    Test for special character in category names
    Test for owner of recipe category
    Test for correct output(recipe category creation)
    Test for deletion of existing recipe category
    Test for editing category names
    Test for editing categorynames with existing categorynames
    """

    def setUp(self):
        """Setting up RecipecategoryClass
        """
        self.recipecategory_class_obj = CategoryClass()

    def tearDown(self):
        """Removing RecipecategoryClass
        """
        del self.recipecategory_class_obj

    def test_existing_recipecategory(self):
        """Check to see category name exists or not
         """
        self.recipecategory_class_obj.recipe_category = \
        [{'owner': 'mary@gmail.com', 'name': 'Breakfast'},
         {'owner': 'mary@gmail.com', 'name': 'Lunch'}]
        response_message = self.recipecategory_class_obj.create_category(
            "Breakfast", "mary@gmail.com")
        self.assertIn("recipe category name already exists.", response_message)

    def test_special_characters(self):
        """Check for special characters in category name
        """
        user = "mary@gmail.com"
        response_message = self.recipecategory_class_obj.create_category("Brea.kf-ast", user)
        self.assertEqual(response_message, "No special characters (. , ! space [] )")

    def test_owner(self):
        """ Check for recipe category belonging to owner"""
        self.recipecategory_class_obj.recipe_category = [{'owner': 'mary@gmail.com', 'name': 'Breakfast'},
                                                 {'owner': 'wanjigi@gmail.com',
                                                  'name': 'Brunch'},
                                                 {'owner': 'mary@gmail.com', 'name': 'Dinner'}]
        user = "mary@gmail.com"
        response_message = self.recipecategory_class_obj.get_owner(user)
        self.assertEqual(response_message, [{'owner': 'mary@gmail.com', 'name': 'Breakfast'}, {
            'owner': 'mary@gmail.com', 'name': 'Dinner'}])

    def test_correct_output(self):
        """Check for correct recipe  category creation
        """
        response_message = self.recipecategory_class_obj.create_category(
            'Dinner', "mary@gmail.com")
        self.assertEqual(
            response_message, [{'owner': 'mary@gmail.com', 'name': 'Dinner'}])

    def test_existing_recipecategory(self):
        """Check for edits to category name
        """
        self.recipecategory_class_obj.recipe_category = [{'owner': 'mary@gmail.com', 'name': 'Lunch'}, {
            'owner': 'mary@gmail.com', 'name': 'Breakfast'}]
        response_message = self.recipecategory_class_obj.edit_category(
            'Dinner', 'Lunch', "mary@gmail.com")
        self.assertEqual(response_message, [{'owner': 'mary@gmail.com', 'name': 'Dinner'}, {
            'owner': 'mary@gmail.com', 'name': 'Breakfast'}])

    def test_edit_existing_recipecategory(self):
        """Check if edit name provided is similar to an existing recipecategory
        """
        self.recipecategory_class_obj.recipe_category = [{'owner': 'mary@gmail.com', 'name': 'Breakfast'}, {
            'owner': 'mary@gmail.com', 'name': 'Lunch'}]
        response_message = self.recipecategory_class_obj.edit_category(
            'Lunch', 'Breakfast', "mary@gmail.com")
        self.assertIn("Recipe category name already exists", response_message)

    def test_delete_recipecategory(self):
        """Check to see if recipecategory is deleted
        """
        self.recipecategory_class_obj.recipe_category = \
        [{'owner': 'mary@gmail.com', 'name': 'Breakfast'}, \
        {'owner': 'mary@gmail.com', 'name': 'Lunch'}, \
        {'owner': 'mary@gmail.com', 'name': 'Dinner'}]
        response_message = self.recipecategory_class_obj.delete_category(
            'Breakfast', "mary@gmail.com")
        self.assertEqual(response_message, \
        [{'owner': 'mary@gmail.com', 'name': 'Lunch'}, \
        {'owner': 'mary@gmail.com', 'name': 'Dinner'}])


if __name__ == '__main__':
    unittest.main()
    
