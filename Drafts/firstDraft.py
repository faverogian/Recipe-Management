import pandas as pd
from collections import Counter, defaultdict
import random

path = r"C:/Users/gmari/OneDrive - University of Windsor/Recipe Management"

# foodList holds the names of the dishes
foodList = {}

foodList["Pastas"] = pd.read_excel(path + "/Food Lists.xlsx", sheet_name="Pastas")["Pastas"].to_list()
foodList["Meats"] = pd.read_excel(path + "/Food Lists.xlsx", sheet_name="Meats")["Meats"].to_list()
foodList["Eggs"] = pd.read_excel(path + "/Food Lists.xlsx", sheet_name="Eggs")["Eggs"].to_list()
foodList["Sides"] = pd.read_excel(path + "/Food Lists.xlsx", sheet_name="Sides")["Sides"].to_list()
foodList["Quick"] = pd.read_excel(path + "/Food Lists.xlsx", sheet_name="Quick")["Quick"].to_list()

# ingredientRef contains the reference for every ingredient used
ingredientRef = pd.read_excel(path + "/Ingredient Classes.xlsx", sheet_name="IngredientRef")
ingredientRef = dict(zip(ingredientRef.Ingredient, ingredientRef.Class))

# ingredientList holds the ingredients needed for each dish
# companionList holds the companions for each dish
ingredientList = {}
companionList = {}

for key in foodList:
    for dish in foodList[key]:
        ingredientList[dish] = pd.read_excel(path + f"/{key}.xlsx", sheet_name=f"{dish}")["Ingredients"].to_list()
        if key != "Sides":
                companions = pd.read_excel(path + f"/{key}.xlsx", sheet_name=f"{dish}")["Companion"].to_list()
                companionList[dish] = [x for x in companions if str(x) != 'nan']

# weekMenu holds the dinners for each day
# dishList is a running tally of the dishes for the week
def pastaChoice():
    pasta = random.choice(foodList["Pastas"])
    companion = ""
    if len(companionList[pasta]) > 0:
        companion = random.choice(companionList[f"{pasta}"])
    return [pasta, companion]
def meatChoice():
    meat = random.choice(foodList["Meats"])
    companion = ""
    if len(companionList[meat]) > 0:
        companion = random.choice(companionList[f"{meat}"])
    return [meat, companion]
def quickChoice():
    quick = random.choice(foodList["Quick"])
    companion = ""
    if len(companionList[quick]) > 0:
        companion = random.choice(companionList[f"{quick}"])
    return [quick, companion]

weekMenu = {}
days = {"Monday": "pasta", "Tuesday": "meat", "Wednesday": "pasta", "Thursday": "quick", "Friday": "pasta"}
dishList = []

for day in days:
    match days[day]:
        case "meat":
            while True:
                [primary,side] = meatChoice()
                if primary not in dishList:
                    break

        case "pasta":
            while True:
                [primary, side] = pastaChoice()
                if primary not in dishList:
                    break

        case "quick":
            [primary, side] = quickChoice()

    dishList += [primary, side]
    if side != "":
        weekMenu[day] = {f"{primary} + {side}"}
    else:
        weekMenu[day] = {f"{primary}"}        

dishList = [x for x in dishList if x != ""]

# shoppingList contains food needed for the week
shoppingList = defaultdict(list)
items = []
for dish in dishList:
    items += ingredientList[dish]
items = dict(Counter(items))

for item in items:
    try:
        category = ingredientRef[f"{item}"]
        shoppingList[f"{category}"].append(item)
    except:
        pass

shoppingList = dict(shoppingList)

# Word Document Output
