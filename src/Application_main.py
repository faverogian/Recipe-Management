'''
Recipe Manager
Application Class
Gian Favero
2022
'''

# Project Imports
from recipeImport import recipeBook
from menuGeneration import weeklyMenuGenerator

# Python Imports
from docxOutput import createDocument
from docx2pdf import convert
import json

json_db = json.load(open('db_recipes.json'))

updatedRecipes = recipeBook(json_db)
weekMenu = weeklyMenuGenerator(updatedRecipes.contents)
createDocument(weekMenu.shoppingList, weekMenu.menu)
convert("Outputs/This_Week_In_Food.docx", 
        "Outputs/This_Week_In_Food.pdf")