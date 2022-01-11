from recipeImport import recipeBook
from menuGeneration import weeklyMenuGenerator
from docxOutput import createDocument
from docx2pdf import convert

path = r"C:/Users/gmari/OneDrive - University of Windsor/Recipe Management/Spreadsheets"

updatedRecipes = recipeBook(path)
weekMenu = weeklyMenuGenerator(path, updatedRecipes.contents)
createDocument(weekMenu.shoppingList, weekMenu.menu)
convert("C:/Users/gmari/OneDrive - University of Windsor/Recipe Management/Outputs/This_Week_In_Food.docx", 
        "C:/Users/gmari/OneDrive - University of Windsor/Recipe Management/Outputs/This_Week_In_Food.pdf")