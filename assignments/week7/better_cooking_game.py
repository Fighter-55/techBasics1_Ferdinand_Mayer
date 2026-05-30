import time
import sys
import csv
import datetime
import random

# Inventory
inventory = []

# Items
items_in_pantry = [
    {"name": "tomato", "type": "food", "description": "A red and ripe fruit."},
    {"name": "egg", "type": "food", "description": "A white egg."},
    {"name": "eggplant", "type": "food", "description": "A soft, purple vegetable."},
    {"name": "bell pepper", "type": "food", "description": "A red, juicy vegetable."},
    {"name": "onion", "type": "food", "description": "A vegetable that is brown and dry from the outside, white and juicy from the inside."},
    {"name": "carrot", "type": "food", "description": "A long orange vegetable."},
    {"name": "lettuce", "type": "food", "description": "Green and juicy leaves."},
    {"name": "celery", "type": "food", "description": "A hard, long and green plant."},
    {"name": "parsley", "type": "garnish", "description": "Green Leaves in a bundle."},
    {"name": "beans", "type": "food", "description": "A can of kidney beans."},
    {"name": "lentils", "type": "food", "description": "Small brown lentils."},
    {"name": "corn", "type": "food", "description": "Sweet yellow corn kernels."},
    {"name": "spices", "type": "food", "description": "A mix of cumin, paprika and chili powder."},
    {"name": "garlic", "type": "food", "description": "A pungent white bulb."},
]

items_in_cupboard = [
    {"name": "kitchen knife", "type": "tool", "description": "A sharp blade with a wooden handle."},
    {"name": "fork", "type": "silverware", "description": "A silver object with three tines"},
    {"name": "spoon", "type": "silverware", "description": "A silver object with a small hollow."},
    {"name": "knife", "type": "silverware", "description": "A silver object with a dull blade."},
    {"name": "pot", "type": "tool", "description": "A metal container with a lid."},
    {"name": "pan", "type": "tool", "description": "A metal hollow with a handle."},
    {"name": "bowl", "type": "tool", "description": "A porcelain hollow."},
    {"name": "cutting board", "type": "tool", "description": "A used wooden board"},
    {"name": "bandage", "type": "healing", "description": "A small sticky plastic object used on cutting wounds."},
]

# Recipes
omelette_recipe = {
    "id": "omelette",
    "name": "Omelette",
    "steps": ["egg", "pan", "egg", "tomato", "parsley"],
    "messages": [
        "You crack the egg.",
        "You whisk the egg together.",
        "You fry the egg in the pan.",
        "You garnish the omelette with tomato.",
        "You garnish the omelette with parsley."
    ]
}

chili_recipe = {
    "id": "chili",
    "name": "Chili sin carne",
    "steps": ["onion", "garlic", "pot", "bell pepper", "pot", "tomato", "beans", "lentils", "corn", "spices", "parsley"],
    "messages": [
        "You chop the onion.",
        "You mince the garlic.",
        "You heat the pot.",
        "You chop the bell pepper.",
        "You add the tomato.",
        "You add the vegetables to the pot.",
        "You add the beans.",
        "You add the lentils.",
        "You add the corn.",
        "You season with spices.",
        "You garnish the chili with parsley."
    ]
}

all_recipes = [omelette_recipe, chili_recipe]

recipe_progress = {recipe["id"]: 0 for recipe in all_recipes}

recipes_used = 0
score = 0

DEBUG = False

long_pause = 2
short_pause = 1


def show_inventory():
    print("Inventory:")
    for item in inventory:
        print(f"- {item['name']}")

def show_pantry():
    print("Pantry:")
    for item in items_in_pantry:
        print(f"- {item['name']}")

def show_cupboard():
    print("Cupboard:")
    for item in items_in_cupboard:
        print(f"- {item['name']}")

def pickup_item(item_name):
    if len(inventory) >= 5:
        print("Your inventory is full!")
        return False
    for item in items_in_pantry:
        if item["name"] == item_name:
            inventory.append(item)
            items_in_pantry.remove(item)
            print("You've picked up", item["name"], "from the pantry")
            return True
    for item in items_in_cupboard:
        if item["name"] == item_name:
            inventory.append(item)
            items_in_cupboard.remove(item)
            print("You've picked up a", item["name"], "from the cupboard")
            return True
    print(f"Could not find '{item_name}'.")
    return False

def drop_item(item_name):
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            if item["type"] == "food" or item["type"] == "garnish":
                items_in_pantry.append(item)
                print("You've put", item["name"], "back in the pantry")
            else:
                items_in_cupboard.append(item)
                print("You've put", item["name"], "back in the cupboard")
            return True
    print(f"'{item_name}' is not in your inventory.")

def examine(item_name):
    for item in inventory + items_in_pantry + items_in_cupboard:
        if item["name"] == item_name:
            print(item["description"])
            print(f"- It is classified as a {item['type']}")
            return True
    print("Item not found.")
    return False

def start_cooking_game():
    print("Congratulations!")
    time.sleep(short_pause)
    print("You have a friend!")
    time.sleep(short_pause)
    print("Unfortunately, you invited them for a dinner and you have to cook for them.")
    time.sleep(short_pause)
    print("Cook both dishes to impress your guest!")
    time.sleep(long_pause)
    print("Type 'recipes' to see what you can cook.")
    time.sleep(short_pause)
    print("Pick up the items you need from the pantry and the cupboard.")
    time.sleep(short_pause)
    print("Type 'help' for a list of commands.")
    time.sleep(short_pause)
    print("Welcome to the cooking game!")
    time.sleep(short_pause)

def main():
    global start_time
    start_time = time.time()
    if DEBUG:
        print("Simulating Cooking...")
        time.sleep(2)
        global score
        score += random.randint(1, 100)
        game_end()
    else:
        start_cooking_game()
        while True:
            command = input("What do you want to do? ").lower().split()
            if not command:
                continue
            if command[0] == "show":
                if len(command) < 2:
                    print("Show what?")
                elif command[1] == "inventory":
                    show_inventory()
                elif command[1] == "pantry":
                    show_pantry()
                elif command[1] == "cupboard":
                    show_cupboard()
                elif command[1] == "leaderboard":
                    show_leaderboard()
            elif command[0] == "pickup":
                pickup_item(" ".join(command[1:]))
            elif command[0] == "drop":
                drop_item(" ".join(command[1:]))
            elif command[0] == "examine":
                examine(" ".join(command[1:]))
            elif command[0] == "cook":
                if len(command) < 2:
                    print("Cook what?")
                elif command[1] == "omelette":
                    cook_recipe(omelette_recipe)
                elif command[1] == "chili":
                    cook_recipe(chili_recipe)
                else:
                    print("Unknown recipe.")
            elif command[0] == "recipes":
                for recipe in all_recipes:
                    print(f"\n{recipe['name']}:")
                    print("Steps: " + ", ".join(recipe["steps"]))
            elif command[0] == "help":
                print(
                    "Commands: show inventory, show pantry, show cupboard, "
                    "pickup [item], drop [item], examine [item], "
                    "cook omelette, cook chili, recipes, help, quit, show leaderboard"
                )
            elif command[0] == "quit":
                game_end()
            elif command[0] == "clear_leaderboard":
                clear_leaderboard()
            else:
                print("Unknown command.")

def is_in_inventory(item_name):
    for item in inventory:
        if item["name"] == item_name:
            return True
    return False

def cook_recipe(recipe):
    global recipes_used
    step = recipe_progress[recipe["id"]]

    if step >= len(recipe["steps"]):
        print(f"You already finished the {recipe['name']}!")
        return

    needed_item = recipe["steps"][step]
    if is_in_inventory(needed_item):
        print(recipe["messages"][step])
        recipe_progress[recipe["id"]] += 1
        print("Good job!")
    else:
        print(f"You need '{needed_item}' in your inventory!")
        return

    if recipe_progress[recipe["id"]] == len(recipe["steps"]):
        recipes_used += 1
        print(f"\nYou finished the {recipe['name']}! ({recipes_used}/{len(all_recipes)} dishes done)")
        if recipes_used == len(all_recipes):
            print("You've cooked everything!")
            game_end()
        else:
            print("Now cook the other dish!")

def game_end():
    score_calculation()
    print("You cooked for your friend!")
    time.sleep(long_pause)
    print("Thank you for playing the cooking game.")
    time.sleep(short_pause)
    name = input("What is your name? ")
    if name == "":
        name = "Anonymous"
    save_record(name, score)
    show_leaderboard()
    sys.exit()

def score_calculation():
    global score
    end_time = time.time()
    total_time = end_time - start_time
    time_bonus = max(0, recipes_used * 500 - int(total_time))
    dish_score = recipes_used * 100
    score = dish_score + time_bonus
    print(f"Your score: {score} ({dish_score} for dishes + {time_bonus} time bonus)")

def save_record(name, score):
    try:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open("records.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([name, score, date])
    except:
        print("Error saving record.")

def show_leaderboard():
    try:
        with open("records.csv", "r") as file:
            reader = csv.reader(file)
            print("\nLeaderboard:")
            sorted_records = sorted(reader, key=lambda row: int(row[1]), reverse=True)
            for row in sorted_records:
                print(f"Name: {row[0]} - Score: {row[1]} - Date: {row[2]}")
    except:
        print("Error loading leaderboard.")

def clear_leaderboard():
    try:
        with open("records.csv", "w") as file:
            pass
        print("Leaderboard cleared.")
    except:
        print("Error clearing leaderboard.")

if __name__ == "__main__":
    main()

# I started this project with a simple cooking game and expanded it step by step with the help of Claude.
# Claude explained concepts to me rather than just giving me the code, which helped me understand what I was doing.
# I learned about dictionaries, global variables, file handling with CSV, and how to structure a larger program.
# Some things like the reader/sorted_records bug or the recipe_progress key error I wouldn't have found on my own.
# And I finally did the game design I originally intended, like the score system and how to make cook_recipe() work for multiple recipes.
# Overall I think this project grew far beyond what I originally planned, and I'm happy with how it turned out.
