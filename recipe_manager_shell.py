from django import db
from Classes.recipeImport import RecipeBook
from Classes.menuGeneration import weeklyMenuGenerator
from Classes.docxOutput import createDocument
from docx2pdf import convert
from cmd import Cmd
from Classes.UserClass import User
import json
import traceback
import sys

class RecipeManagementShell(Cmd):
    """
    A class used to provide a command-line interface with the Recipe Manager
    """
    intro = "The Recipe Manager, 2022. Type help or ? to list commands.\n"
    prompt = "Recipe Manager> "

    def __init__(self):
        super().__init__(self)
        self.db = json.load(open('db_recipes.json'))
        self.user = None

    def do_login(self, args):
        """
        Login to a user session
        """
        if self.user is None:
            self.user = User(self.db)
            self.user.log_in()
            # Reassign current user to None if login was terminated
            if not self.user.isLoggedIn:
                self.user = None
        else:
            print(f"{self.user.username} is already logged in\n")

    def do_logout(self, args):
        """
        Logout of a user session
        """
        if self.user is None:
            print("Nobody is logged in\n")
        else:
            print(f"{self.user.username} has been logged out\n")
            self.user = None
    
    def do_pick_meals(self, args):
        """
        Generate a week's menu and shopping list for the week
        """
        if self.user is not None:
            self.user.pick_meals()
        else:
            print("You must login first!")

    def do_new_meal(self, args):
        """
        Add a new meal to a User's database
        """
        if self.user is not None:
            self.user.new_meal()
        else:
            print("You must login first!")
    
    def do_exit(self, args):
        """
        Exit the Recipe Manager Shell
        """
        sys.exit()

def main():
    try:
        prompt = RecipeManagementShell()
    except:
        print("Exiting...")
        sys.exit()
    prompt.cmdloop()

if __name__ == '__main__':
    main()
