FRUITS = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grape": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80
}

def main():
    # Prompt user for fruits
    fruit = input("Item: ").title()

    # Calculate the calories attributed every fruit
    calories = calories_scale(fruit)

    # Output calories of every item inputted, and ignore inputs that aren't fruits
    if calories is not None:
          print(f"Calories: {calories}")

# Define functions that calculates calories of every fruit in the fruit dictionary
def calories_scale(f):
       return FRUITS.get(f, None)


main()
