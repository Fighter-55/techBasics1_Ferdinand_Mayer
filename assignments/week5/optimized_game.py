import time
import sys

# defining variables
PAUSE_SHORT = 1
PAUSE_MEDIUM = 1.5
PAUSE_LONG = 2
PAUSE_DRAMATIC = 3
cave_counter = 1

# starting the game
def game_initiation():
    global cave_counter
    cave_counter = 1
    print("You are an adventurer.")
    time.sleep(PAUSE_SHORT)
    print("You wake up in a dark forest.")
    time.sleep(PAUSE_SHORT)
    print("You lay by a path going either left or right.")
    time.sleep(PAUSE_MEDIUM)
    way_selection()

# function for the first path selection
def way_selection():
    way = ask_question("Which way do you want to go?", ["left", "right"])
    if way == "left":
        print("You go left.")
        way1_left()
    else:
        print("You go right.")
        way1_right()

# function for the left side of the forrest
def way1_left():
    time.sleep(PAUSE_LONG)
    print("You continue deeper into the forest.")
    time.sleep(PAUSE_LONG)
    print("You come to a clearing.")
    time.sleep(PAUSE_SHORT)
    print("You see a tree.")
    time.sleep(PAUSE_SHORT)
    print("An elf sits in the tree.")
    time.sleep(PAUSE_SHORT)
    print("He asks you if you want to play a game.")
    time.sleep(PAUSE_MEDIUM)
    elf_selection()

# function for the right side of the forrest
def way1_right():
    time.sleep(PAUSE_LONG)
    print("You continue deeper into the forest.")
    time.sleep(PAUSE_LONG)
    print("You see Mountains in the distance.")
    time.sleep(PAUSE_SHORT)
    print("You see a cave.")
    time.sleep(PAUSE_MEDIUM)
    cave_selection()

# function for choosing the elf or the forrest
def elf_selection():
    answer = ask_question("Do you want to play a game?", ["yes", "no"])
    if answer == "yes":
        time.sleep(PAUSE_MEDIUM)
        elf_game()
    else:
        print("You continue on your way.")
        time.sleep(PAUSE_SHORT)
        print("You go back into the forest.")
        time.sleep(PAUSE_SHORT)
        print("The ground is covered with leaves.")
        time.sleep(PAUSE_SHORT)
        print("You fall into a pit and get eaten by Goblins.")
        time.sleep(PAUSE_DRAMATIC)
        game_end()

# playing a game with the elf
def elf_game():
    print("You play a game.")
    time.sleep(PAUSE_SHORT)
    print("The elf wants you to roll a dice with 6 sides.")
    time.sleep(PAUSE_SHORT)
    print("If you roll an even number, you get to have dinner with the elf.")
    time.sleep(PAUSE_SHORT)
    print("If you roll an odd number, he gets all of your stuff and you have to work in his mine.")
    time.sleep(PAUSE_DRAMATIC)
    dice_roll()

# function for the elf dice roll
def dice_roll():
    roll = ask_question("What number do you roll?", ["1", "2", "3", "4", "5", "6"])
    if roll in ["2", "4", "6"]:
        print("You get to have dinner with the elf.")
        time.sleep(PAUSE_SHORT)
        print("You eat some mushrooms.")
        time.sleep(PAUSE_SHORT)
        print("You go onto a hell of a Trip and run into the forest.")
        time.sleep(PAUSE_MEDIUM)
        print("You pass out and get eaten by a pack of wolves.")
        time.sleep(PAUSE_DRAMATIC)
        game_end()
    else:
        print("He strips you and vanishes.")
        time.sleep(PAUSE_SHORT)
        print("You freeze to death.")
        time.sleep(PAUSE_DRAMATIC)
        game_end()

# function for choosing between the cave and the mountains
def cave_selection():
    answer = ask_question("Do you want to enter the cave?", ["yes", "no"])
    if answer == "yes":
        print("You enter the cave.")
        time.sleep(PAUSE_SHORT)
        print("The Cave is dark and you can't see anything.")
        time.sleep(PAUSE_SHORT)
        print("You find a lighter in your pocket.")
        time.sleep(PAUSE_SHORT)
        print("You ignite the lighter.")
        time.sleep(PAUSE_SHORT)
        cave_path()
    else:
        print("You continue on your way.")
        time.sleep(PAUSE_SHORT)
        mountains_selection()

# function for going to the mountains
def mountains_selection():
    answer = ask_question("Do you want to go up the mountains?", ["yes", "no"])
    if answer == "yes":
        print("You go into the mountains.")
        time.sleep(PAUSE_SHORT)
        print("You walk through Snow.")
        time.sleep(PAUSE_SHORT)
        print("The Snow collapses and you fall into a crevice.")
        time.sleep(PAUSE_MEDIUM)
        print("You survive the Fall but freeze to death.")
        time.sleep(PAUSE_DRAMATIC)
        game_end()
    else:
        print("You continue on your way.")
        time.sleep(PAUSE_SHORT)
        way1_left()

# function for the cave selections
def cave_path():
    global cave_counter
    def cave_question(player_answer, cave_direction):
        global cave_counter
        if player_answer == cave_direction :
            cave_counter += 1
            cave_path()
        elif answer == "turnaround":
            mountains_selection()
        else:
            cave_spiders()
    print("You continue deeper into the cave.")
    time.sleep(PAUSE_SHORT)
    print("The path of the cave splits.")
    time.sleep(PAUSE_MEDIUM)
    answer = ask_question("Which way do you want to go?", ["left", "right", "turnaround"])
    if cave_counter == 1:
        cave_question(answer, "left")
    elif cave_counter == 2:
        cave_question(answer, "right")
    elif cave_counter == 3:
        cave_question(answer, "left")
    elif cave_counter == 4:
        cave_question(answer, "left")
    elif cave_counter == 5:
        if answer == "right":
            cave_counter += 1
            cave_path()
        elif answer == "turnaround":
            turnaround()
        else:
            cave_spiders()
    else:
        cave_spiders()

# winning function inside the cave
def turnaround():
    print("You turn around.")
    time.sleep(PAUSE_SHORT)
    print("You stumble across a chest you haven't seen before.")
    time.sleep(PAUSE_SHORT)
    print("You open the chest and find a magic wand.")
    time.sleep(PAUSE_SHORT)
    print("You exit the cave.")
    time.sleep(PAUSE_SHORT)
    print("You hold the wand up into the air")
    time.sleep(PAUSE_SHORT)
    print("A white light appears in the sky.")
    time.sleep(PAUSE_SHORT)
    print("You fly up into the sky and see the Landscape you were in.")
    time.sleep(PAUSE_SHORT)
    print("You wake up in your bed.")
    time.sleep(PAUSE_SHORT)
    print("You realise that it was all a dream.")
    time.sleep(PAUSE_DRAMATIC)
    game_end()

# Spiders
def cave_spiders():
    print("As you walk deeper into the cave you smell rotten flesh.")
    time.sleep(PAUSE_SHORT)
    print("You look to the ceiling and see little white rocks attached.")
    time.sleep(PAUSE_SHORT)
    print("As You look up you step into one of the rocks.")
    time.sleep(PAUSE_SHORT)
    print("You realise that the white rocks are spider eggs.")
    time.sleep(PAUSE_SHORT)
    print("The cracking of the egg awakens thousands of little spiders and a huge momma Spider.")
    time.sleep(PAUSE_MEDIUM)
    print("You are the feast of a new generation of horrifying spiders")
    time.sleep(PAUSE_DRAMATIC)
    game_end()

# Function for asking Questions and leaving the Game
def ask_question(question, valid_answers):
    while True:
        answer = input(question).lower()
        if answer in valid_answers:
            return answer
        elif answer == "exit":
            game_end()
        else:
            print( "Invalid answer. If you want to exit enter 'exit' Otherwise please enter one of the following: " + ", ".join(valid_answers))

# Game End
def game_end():
    answer = ask_question("Do you want to play again?", ["yes", "no"])
    if answer == "yes":
        game_initiation()
    else:
        print("Thanks for playing!")
        sys.exit()

if __name__ == "__main__":
    game_initiation()

# for the optimization I let Claude AI analyse the Code and give me suggestions for optimizing it.
# It suggested the global time parameters but the simplifying of the cave section was my own Idea.
# Claude AI helped me a lot to understand the Code and gave me "breadcrumbs" for finding the final solution.
# I never used AI to create code only to understand it.