""" test_userclass.py"""
import sys
import unittest
# import module useraccounts
from app.userclass import User


class AccountTestCases(unittest.TestCase):
    """
    Test for duplicate accounts(user already exists)
    Test for short passwords
    Test for correct output/account creation
    Test login with no account
    Test login with wrong password
    Test login with existing email and password
    """

    def setUp(self):
        """Setting up UserClass before anything
        """
        self.user = User()

    def tearDown(self):
        """Removing UserClass after everything
        """
        del self.user

    def test_case_pwd_equals_cpwd(self):
        """
        Args
            password =! confirm password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Eunice", "eunicegatehi@gmail.com", "eunicegatehi", "eunicegatehiw")
        self.assertEqual( msg, "Password mismatch")
    def test_case_short_pwd(self):
        """
        Args
            username
            email
            short password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Eunice", "gatehieunice@gmail.com", "eunce", "eunce")
        self.assertEqual(
            msg, "Your password should be at least 6 characters long")

    def test_case_existing_user(self):
        """
        Args
            registered user
        Returns
            error message
        """
        self.user.registeruser(
            "Eunice", "eunicegatehi@gmail.com", "eunicegatehi", "eunicegatehi")
        msg = self.user.registeruser(
            "Eunice", "eunicegatehi@gmail.com", "eunicegatehi", "eunicegatehi")
        self.assertIn("User already exists", msg)

    def test_case_special_char(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Eun!c$", "eunicegatehi@gmail.com", "eunice", "eunice")
        self.assertIn( msg, "No special characters (. , ! space [] )")

    def test_case_invalid_email(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Eunice", "eunicegatehi@gmail", "eunicegatehi", "eunicegatehi")
        self.assertEqual(msg, "Please provide a valid email address")

    def test_case_correct_input(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            success message
        """
        msg = self.user.registeruser(
            "Eunice", "eunicegatehi@gmail.com", "eunicegatehi", "eunicegatehi")
        self.assertIn("Successfully registered. You can now login", msg)

    def test_case_login_noaccount(self):
        """
        Args
            non existent email and password
        Returns
            error message
        """
        self.user.user_list = [
            {'username': 'eunice', 'password': 'eunicegatehi', 'email': 'eunicegatehi@gmail.com'}]
        msg = self.user.login("wanjigi@gmail.com", "wanjigi")
        self.assertEqual(msg, "You have no account,please sign up")

    def test_case_login_wrong_password(self):
        """
        Args
            existent email and wrong password
        Returns
            error message
        """
        self.user.user_list = [
            {'username': 'eunice', 'password': 'eunicegatehi', 'email': 'euicegatehiw@gmail.com'}]
        msg = self.user.login("euicegatehiw@gmail.com", "gatehieunice")
        self.assertEqual(msg, "Password mismatch")

    def test_case_correct_login(self):
        """
        Args
            existent email and password
        Returns
            success message
        """
        self.user.user_list = [
            {'username': 'eunice', 'password': 'eunicegatehi', 'email': 'eunicegatehiw@gmail.com'}]
        msg = self.user.login("eunicegatehiw@gmail.com", "eunicegatehi")
        self.assertIn("Successfully logged in, create recipecategory!", msg)


if __name__ == '__main__':
    unittest.main()