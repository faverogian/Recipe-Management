from Classes.recipeImport import RecipeBook
from Classes.menuGeneration import weeklyMenuGenerator
import webbrowser
import difflib

class User(): 
    """
    Representation of a user in the Recipe Manager suite.
    """
    def __init__(self, db):
        # Raw .json db file
        self.db  = db

        # User variables
        self.isLoggedIn = False
        self.username = ""
        self.recipeBook = {}
        self.schedule = {}

    def log_in(self):
        """
        Validates that the username entered is in the .json db file and puts user into
        a logged in state.
        """
        print("\nUser Authentication")

        while (not self.isLoggedIn):
            # Take User ID input from the user
            self.username = "Gian" #input("User ID: ")

            # Check if User ID exists in .json db
            for user in self.db["Users"]:
                if self.username == user["Name"]:
                    print("Logged in successfully!\n")

                    # Import the user's recipeBook list
                    self.recipeBook = RecipeBook(user)

                    self.isLoggedIn = True

            # If User ID is not found, ask to try again
            if not self.isLoggedIn:
                try_again = input("Invalid User ID. Try Again? (y/n): ")
                if try_again == "n":
                    break

    def pick_meals(self):
        """
        Creates the week's menu and shopping list and opens the .pdf 
        in a new browser window
        """
        print("Choosing this week's meals...")
        print("Creating this week's shopping list...")
        self.weekMenu = weeklyMenuGenerator(self.recipeBook).outputFile
        webbrowser.open_new(self.weekMenu)

    def new_meal(self):
        """
        Adds a new meal to the user's database
        """
        mealName = ""
        mealGenre = ""
        mealIngredients = []

        mealName = input("Enter name of new meal (Or enter 'stop' to abort): ").title()
        if mealName == "Stop":
            return
        elif mealName in self.recipeBook.ingredientListByMeal.keys():
            print("Meal already exists")
            return

        while True:
            mealGenre = input("Enter genre of meal (Or enter '?' to view options or 'stop' to abort): ").title()
            if mealGenre == "?":
                for genre in self.recipeBook.mealListByGenre.keys():
                    print(f"{genre}")
            elif mealGenre in self.recipeBook.mealListByGenre.keys():
                break
            elif mealGenre == "Stop":
                return
            else:
                matchFound = False
                closeMatches = difflib.get_close_matches(mealGenre, self.recipeBook.mealListByGenre.keys())
                for closeMatch in closeMatches:
                    while True:
                        acceptMatch = input(f"Did you mean '{closeMatch}'? ('yes'/'no'): ").lower()
                        if acceptMatch in "yes":
                            mealGenre = closeMatch
                            matchFound = True
                            break
                        elif acceptMatch in "no":
                            break
                        else:
                            continue

                    if matchFound:
                        break
                    
                if not matchFound:
                    addGenre = input(f"Meal genre '{mealGenre}' not found in database. Add '{mealGenre}' to database? ('yes'/'no'): ")
                    if addGenre in "yes":
                        break

        print("\nEnter ingredients one-by-one: \n")
        while True:
            ingredient = input("Add Ingredient (Enter 'done' when finished or 'stop' to abort): ").title()
            if ingredient == "Stop":
                return
            elif ingredient == "Done":
                break
            
            matchFound = False
            if ingredient in self.recipeBook.totalIngredientList:
                matchFound = True
                mealIngredients.append(ingredient)

            if not matchFound:
                closeMatches = difflib.get_close_matches(ingredient, self.recipeBook.totalIngredientList)
                for closeMatch in closeMatches:
                    acceptMatch = input(f"Did you mean '{closeMatch}'? ('yes'/'no'): ")
                    if acceptMatch.lower() in "yes":
                        matchFound = True
                        mealIngredients.append(closeMatch)
                    else:
                        continue
                    break

                if not matchFound:
                    addIngredient = (f"Ingredient: '{ingredient}' not found in database. Add '{ingredient}' to database? ('yes'/'no'): ")
                    if addIngredient.lower() in "yes":
                        while True:
                            type = input("Enter Ingredient Type (Enter '?' to view options or 'stop' to abort): ").title()
                            if type == "?":
                                for type in self.recipeBook.ingredientRef.keys():
                                    print(type)
                            elif type == "Stop":
                                break
                            elif type in self.recipeBook.ingredientRef.keys():
                                self.recipeBook.ingredientRef[genre].append(ingredient)
                                mealIngredients.append(ingredient)
                                break
                            else:
                                print("Invalid Option")
                    else:
                        print("Ingredient not added to database.")







        
        
        



