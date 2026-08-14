class Recipe():
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time

    def __str__(self):
        return (f"""Name: {self.name}
Ingredients: {self.ingredients}
Cooking time: {self.cooking_time}""")
        

def main():
    print("Welcome to Recipe Collection")
    recipe = get_recipe() 
    print("\ndisplaying recipe")
    print(recipe)

def get_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients: ")
    cooking_time = input("Enter cooking time: ")

    return Recipe(name, ingredients, cooking_time)


if __name__=="__main__":
    main()