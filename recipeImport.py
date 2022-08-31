'''
Recipe Manager
Recipe Book Class
Gian Favero
2022
'''

class recipeBook:
    def __init__(self, json_db):
        self.db = json_db
        self.foodGenres = ["Pastas", "Meats", "Quick", "Sides"]
        self.foodList = {}
        self.ingredientRef = {}
        self.ingredientList = {}
        self.companionList = {}

        self.updateFoodLists()
        self.updateIngredientRef()
        self.contents = [self.foodList, self.ingredientRef, self.ingredientList, self.companionList]
    
    def updateFoodLists(self):
        for genre in self.foodGenres:
            self.foodList[genre] = []
            for item in self.db["Meals"][genre]:
                self.foodList[genre].append(item["Name"])
                self.ingredientList[item["Name"]] = item["Ingredients"]
                if genre != "Sides":
                    self.companionList[item["Name"]] = item["Companions"]

    def updateIngredientRef(self):
        self.ingredientRef = self.db["Ingredient Classes"]

