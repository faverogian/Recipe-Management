'''
Recipe Manager
Menu Generation Class
Gian Favero
2022
'''

# Python Imports
from collections import Counter, defaultdict
import random

class weeklyMenuGenerator:
    def __init__(self, recipeBook) -> None:
        self.foodList = recipeBook[0]
        self.ingredientRef = recipeBook[1]
        self.ingredientList = recipeBook[2]
        self.companionList = recipeBook[3]
        self.days = {"Monday": "pasta", "Tuesday": "meat", "Wednesday": "pasta", "Thursday": "quick", "Friday": "pasta"}
        self.menu = {}
        self.dishList = []
        self.items = []
        self.shoppingList = defaultdict(list)

        self.pickMeals()
        self.createShoppingList()

    def pastaChoice(self):
        pasta = random.choice(self.foodList["Pastas"])
        companion = ""
        if len(self.companionList[pasta]) > 0:
            companion = random.choice(self.companionList[f"{pasta}"])
        return [pasta, companion]

    def meatChoice(self):
        meat = random.choice(self.foodList["Meats"])
        companion = ""
        if len(self.companionList[meat]) > 0:
            companion = random.choice(self.companionList[f"{meat}"])
        return [meat, companion]

    def quickChoice(self):
        quick = random.choice(self.foodList["Quick"])
        companion = ""
        if len(self.companionList[quick]) > 0:
            companion = random.choice(self.companionList[f"{quick}"])
        return [quick, companion]

    def pickMeals(self):
        for day in self.days:
            if self.days[day] == "meat":
                while True:
                    [primary,side] = self.meatChoice()
                    if primary not in self.dishList:
                        break

            elif self.days[day] == "pasta":
                while True:
                    [primary, side] = self.pastaChoice()
                    if primary not in self.dishList:
                        break

            elif self.days[day] == "quick":
                [primary, side] = self.quickChoice()

            self.dishList += [primary, side]
            if side != "":
                self.menu[day] = {f"{primary} + {side}"}
            else:
                self.menu[day] = {f"{primary}"}        

        self.dishList = [x for x in self.dishList if x != ""]
    
    def createShoppingList(self):
        items = []
        for dish in self.dishList:
            items += self.ingredientList[dish]
        items = dict(Counter(items))

        for item in items:
            for category in self.ingredientRef:
                if item in self.ingredientRef[category]:
                    self.shoppingList[category].append(item)
    
        # Routine items to check for on a weekly basis
        if "White Bread" not in self.shoppingList["Bakery"]:
            self.shoppingList["Bakery"] += ["White Bread"]
        if "Milk" not in self.shoppingList["Dairy"]:
            self.shoppingList["Dairy"] += ["Milk"]
        self.shoppingList["Bakery"] += ["Baguette"]
        self.shoppingList = dict(self.shoppingList)
