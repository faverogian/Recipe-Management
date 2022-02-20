from collections import Counter, defaultdict
from Classes.recipeImport import RecipeBook
import random

from Classes.docxOutput import createDocument

class weeklyMenuGenerator:
    """
    Class that takes in a user's recipe book and generates a week's menu and shopping list
    """
    def __init__(self, recipeBook: RecipeBook) -> None:
        # Import information by parsing the recipeBook contents
        self.mealListByGenre = recipeBook.mealListByGenre
        self.ingredientRef = recipeBook.ingredientRef
        self.ingredientListByMeal = recipeBook.ingredientListByMeal
        self.companionListByMeal = recipeBook.companionListByMeal
        self.schedule = recipeBook.schedule

        # Variables to be filled in...
        self.menu = {}
        self.dishList = []
        self.items = []
        self.shoppingList = defaultdict(list)

        # Fill in those variables
        self.pickMeals()
        self.createShoppingList()
        self.outputFile = createDocument(self.shoppingList, self.menu)

    def pastaChoice(self):
        pasta = random.choice(self.mealListByGenre["Pastas"])
        companion = ""
        if len(self.companionListByMeal[pasta]) > 0:
            companion = random.choice(self.companionListByMeal[f"{pasta}"])
        return [pasta, companion]

    def meatChoice(self):
        meat = random.choice(self.mealListByGenre["Meats"])
        companion = ""
        if len(self.companionListByMeal[meat]) > 0:
            companion = random.choice(self.companionListByMeal[f"{meat}"])
        return [meat, companion]

    def quickChoice(self):
        quick = random.choice(self.mealListByGenre["Quick"])
        companion = ""
        if len(self.companionListByMeal[quick]) > 0:
            companion = random.choice(self.companionListByMeal[f"{quick}"])
        return [quick, companion]

    def pickMeals(self):
        for day in self.schedule:
            match self.schedule[day].lower():
                case "meat":
                    while True:
                        [primary,side] = self.meatChoice()
                        if primary not in self.dishList:
                            break

                case "pasta":
                    while True:
                        [primary, side] = self.pastaChoice()
                        if primary not in self.dishList:
                            break

                case "quick":
                    [primary, side] = self.quickChoice()

            self.dishList += [primary, side]
            if side != "":
                self.menu[day] = {f"{primary} + {side}"}
            else:
                self.menu[day] = {f"{primary}"}        

        self.dishList = [x for x in self.dishList if x != ""]
    
    def createShoppingList(self):
        items = []
        for meal in self.dishList:
            items += self.ingredientListByMeal[meal]
        items = dict(Counter(items))

        for item in items:
            for category in self.ingredientRef:
                if item in self.ingredientRef[category]:
                    self.shoppingList[category].append(item)