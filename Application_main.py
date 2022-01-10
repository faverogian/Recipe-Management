from recipeImport import recipeBook
from menuGeneration import weeklyMenuGenerator
from docxOutput import createDocument

path = r"C:/Users/gmari/OneDrive - University of Windsor/Recipe Management/Spreadsheets"

updatedRecipes = recipeBook(path)
weekMenu = weeklyMenuGenerator(path, updatedRecipes.contents)
createDocument(weekMenu.shoppingList, weekMenu.menu)