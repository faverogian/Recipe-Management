from collections import Counter, defaultdict
import random

class weeklyMenuGenerator:
    def __init__(self, path, recipeBook) -> None:
        self.path = path
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
            match self.days[day]:
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
        for dish in self.dishList:
            items += self.ingredientList[dish]
        items = dict(Counter(items))

        for item in items:
            try:
                category = self.ingredientRef[f"{item}"]
                self.shoppingList[f"{category}"].append(item)
            except:
                print(f"Error generating shopping list: {item} not found in database.")
                pass
    
        # Routine items to check for
        if "White Bread" not in self.shoppingList["Bakery"]:
            self.shoppingList["Bakery"] += ["White Bread"]
        if "Milk" not in self.shoppingList["Dairy"]:
            self.shoppingList["Dairy"] += ["Milk"]
        self.shoppingList["Bakery"] += ["Baguette"]
        self.shoppingList["Snacks"] += ["Granola Bars", "Fishie Crackers", "Nutella", "Lunch Meat"]
        self.shoppingList = dict(self.shoppingList)
