import time
import sys

def game_initiation():
    print("You are an adventurer.")
    time.sleep(1)
    print("You wake up in a dark forrest.")
    time.sleep(1)
    print("You lay by a path going either left or right.")
    time.sleep(2)
    way_selection()

def way_selection():
    way = ask_question("Which way do you want to go?", ["left", "right"])
    if way == "left":
        print("You go left.")
        way1_left()
    else:
        print("You go right.")
        way1_right()

def way1_left():
    time.sleep(1.5)
    print("You continue deeper into the forrest.")
    time.sleep(1.5)
    print("You come to a clearing.")
    time.sleep(0.5)
    print("You see a tree.")
    time.sleep(0.2)
    print("An elf sits in the tree.")
    time.sleep(0.5)
    print("He asks you if you want to play a game.")
    time.sleep(2)
    elf_selection()

def way1_right():
    time.sleep(1.5)
    print("You continue deeper into the forrest.")
    time.sleep(1.5)
    print("You see Mountains in the distance.")
    time.sleep(1)
    print("You see a cave.")
    time.sleep(2)
    cave_selection()

def elf_selection():
    answer = ask_question("Do you want to play a game?", ["yes", "no"])
    if answer == "yes":
        print("You play a game.")
        time.sleep(2)
        elf_game()
    else:
        print("You continue on your way.")
        time.sleep(1)
        print("You go back into the forrest.")
        time.sleep(1)
        print("The ground is covered with leaves.")
        time.sleep(0.5)
        print("You fall into a pit and get eaten by Goblins.")
        time.sleep(3)
        game_end()

def elf_game():
    print("You play a game.")
    time.sleep(0.3)
    print("The elf wants you to roll a dice with 6 sides.")
    time.sleep(1)
    print("If you roll an even number, you get to have dinner with the elf.")
    time.sleep(1)
    print("If you roll an odd number, he gets all of your stuff and you have to work in his mine.")
    time.sleep(3)
    dice_roll()

def dice_roll():
    roll = ask_question("What number do you roll?", ["1", "2", "3", "4", "5", "6"])
    if roll in [2,4,6]:
        print("You get to have dinner with the elf.")
        time.sleep(1)
        print("You eat some mushrooms.")
        time.sleep(1)
        print("You go onto a hell of a Trip and run into the forrest.")
        time.sleep(2)
        print("You pass out and get eaten by a pack of wolves.")
        time.sleep(3)
        game_end()
    else:
        print("He strips you and vanishes.")
        time.sleep(1)
        print("You freeze to death.")
        time.sleep(3)
        game_end()

def cave_selection():
    answer = ask_question("Do you want to enter the cave?", ["yes", "no"])
    if answer == "yes":
        print("You enter the cave.")
        time.sleep(1)
        cave1()
    else:
        print("You continue on your way.")
        time.sleep(1)
        mountains_selection()

def mountains_selection():
    answer = ask_question("Do you want to go up the mountains?", ["yes", "no"])
    if answer == "yes":
        print("You go into the mountains.")
        time.sleep(1)
        print("You walk through Snow.")
        time.sleep(1)
        print("The Snow collapses and you fall into a crevice.")
        time.sleep(2)
        print("You survive the Fall but freeze to death.")
        time.sleep(3)
        game_end()
    else:
        print("You continue on your way.")
        time.sleep(1)
        way1_left()

def cave1():
    print("The Cave is dark and you can't see anything.")
    time.sleep(1)
    print("You find a lighter in your pocket.")
    time.sleep(1)
    print("You egnite the lighter.")
    time.sleep(1)
    print("The path of the cave splits.")
    time.sleep(2)
    answer = ask_question("Which way do you want to go?", ["left", "right"])
    if answer == "left":
        print("You go left.")
        time.sleep(1)
        cave_way1_left()
    else:
        print("You go right.")
        time.sleep(1)
        cave_spiders()

def cave_way1_left():
    print("You continue deeper into the cave.")
    time.sleep(1)
    print("The path of the cave splits.")
    answer = ask_question("Which way do you want to go?", ["left", "right"])
    if answer == "right":
        print("You go right.")
        time.sleep(1)
        cave_way2_right()
    else:
        print("You go left.")
        time.sleep(1)
        cave_spiders()

def cave_way2_right():
    print("You continue deeper into the cave.")
    time.sleep(1)
    print("The path of the cave splits.")
    answer = ask_question("Which way do you want to go?", ["left", "right"])
    if answer == "left":
        print("You go left.")
        time.sleep(1)
        cave_way3_left()
    else:
        print("You go right.")
        time.sleep(1)
        cave_spiders()

def cave_way3_left():
    print("You continue deeper into the cave.")
    time.sleep(1)
    print("The path of the cave splits.")
    answer = ask_question("Which way do you want to go?", ["left", "right"])
    if answer == "right":
        print("You go right.")
        time.sleep(1)
        cave_way4_right()
    else:
        print("You go left.")
        time.sleep(1)
        cave_spiders()

def cave_way4_right():
    print("You continue deeper into the cave.")
    time.sleep(1)
    print("The path of the cave splits.")
    answer = ask_question("Which way do you want to go?", ["left", "right", "turnaround"])
    if answer == "right":
        print("You go right.")
        time.sleep(1)
        cave_way5_right()
    elif answer == "turnaround":
        print("You turn around.")
        time.sleep(1)
        print("You stumble across a chest you haven't seen before.")
        time.sleep(1)
        print("You open the chest and find a magic wand.")
        time.sleep(1)
        print("You exit the cave.")
        time.sleep(1)
        print("You hold the wand up into the air")
        time.sleep(1)
        print("A white light appears in the sky.")
        time.sleep(1)
        print("You fly up into the sky and see the Landscape you were in.")
        time.sleep(1)
        print("You wake up in your bed.")
        time.sleep(1)
        print("You realise that it was all a dream.")
        time.sleep(3)
        game_end()
    else:
        print("You go left.")
        time.sleep(1)
        cave_spiders()

def cave_way5_right():
    print("You continue deeper into the cave.")
    time.sleep(1)
    print("The path of the cave splits.")
    answer = ask_question("Which way do you want to go?", ["left", "right"])
    if answer == "right":
        print("You go right.")
        time.sleep(1)
        cave_spiders()
    else:
        print("You go left.")
        time.sleep(1)
        cave_spiders()

# Spiders
def cave_spiders():
    print("As you walk deeper into the cave you smell rotten flesh.")
    time.sleep(1)
    print("You look to the ceiling and see little white rocks attached.")
    time.sleep(1)
    print("As You look up you step into one of the rocks.")
    time.sleep(1)
    print("You realise that the white rocks are spider eggs.")
    time.sleep(1)
    print("The cracking of the egg awakens thousands of little spiders and a huge momma Spider.")
    time.sleep(2)
    print("You are the feast of a new generation of horrifying spiders")
    time.sleep(3)
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

game_initiation()
