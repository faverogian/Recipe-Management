class RecipeBook:
    """
    Class representing a User's recipe book
    """
    def __init__(self, user_db):
        self.user_db = user_db
        self.ingredientRef = user_db["Ingredient Classes"]  # {IngredientClass: [Ingredients]}
        self.schedule = user_db["Schedule"]                 # {Day: MealGenre}
        self.mealGenres = user_db["Meals"].keys()           # [MealGenres]

        # Lists to be filled in...
        self.mealListByGenre = {}                           # {MealGenre: [Meals]}
        self.ingredientListByMeal = {}                      # {MealName: [Ingredients]}
        self.companionListByMeal = {}                       # {MealName: [CompanionDishes]
        self.totalIngredientList = []                       # [Ingredients]

        # Fill in those lists
        self.importRecipeBook()

        # Pack all information into a passable variable
        self.contents = {"Genre-Meal List": self.mealListByGenre,
                         "Meal-Ingredient List": self.ingredientListByMeal,
                         "Meal-Companion List": self.companionListByMeal,
                         "Schedule": self.schedule,
                         "Ingredient Ref": self.ingredientRef,
                         "Total Ingredient List": self.totalIngredientList}
    
    def importRecipeBook(self):
        """
        Imports a user's recipe book
        """
        for genre in self.mealGenres:
            self.mealListByGenre[genre] = []
            for item in self.user_db["Meals"][genre]:
                self.mealListByGenre[genre].append(item["Name"])
                self.ingredientListByMeal[item["Name"]] = item["Ingredients"]
                if genre != "Sides":
                    self.companionListByMeal[item["Name"]] = item["Companions"]

        for key in self.ingredientRef.keys():
            self.totalIngredientList.extend(self.ingredientRef[key])