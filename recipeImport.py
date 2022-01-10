import pandas as pd

class recipeBook:
    def __init__(self, path):
        self.path = path
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
            self.foodList[f"{genre}"] = pd.read_excel(self.path + "/Food Lists.xlsx", sheet_name=f"{genre}")[f"{genre}"].to_list()

        for key in self.foodList:
            for dish in self.foodList[key]:
                self.ingredientList[dish] = pd.read_excel(self.path + f"/{key}.xlsx", sheet_name=f"{dish}")["Ingredients"].to_list()
                if key != "Sides":
                        companions = pd.read_excel(self.path + f"/{key}.xlsx", sheet_name=f"{dish}")["Companion"].to_list()
                        self.companionList[dish] = [x for x in companions if str(x) != 'nan']

    def updateIngredientRef(self):
        self.ingredientRef = pd.read_excel(self.path + "/Ingredient Classes.xlsx", sheet_name="IngredientRef")
        self.ingredientRef = dict(zip(self.ingredientRef.Ingredient, self.ingredientRef.Class))

