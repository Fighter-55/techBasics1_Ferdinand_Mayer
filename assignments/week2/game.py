import time

def game_initiation():
    print("You are an adventurer.")
    time.sleep(1)
    print("You wake up in a dark forrest.")
    time.sleep(1)
    print("You lay by a path going either left or right.")
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
    print("You go left.")
    time.sleep(1.5)
    print("You continue deeper into the forrest.")
    time.sleep(1.5)
    print("You come to a clearing.")
    time.sleep(0.5)
    print("You see a tree.")
    time.sleep(0.2)
    print("An elf sits in the tree.")
    print("He asks you if you want to play a game.")
    elf_selection()

def way1_right():
    print("You go right.")
    time.sleep(1.5)
    print("You continue deeper into the forrest.")
    time.sleep(1.5)
    print("You see hills.")
    time.sleep(1)
    print("You see a cave.")
    cave_selection()

def elf_selection():
    answer = ask_question("Do you want to play a game?", ["yes", "no"])
    if answer == "yes":
        print("You play a game.")
        elf_game()
    else:
        print("You continue on your way.")
        time.sleep(1)
        print("You go back into the forrest.")
        time.sleep(1)
        print("The ground is covered with leaves.")
        time.sleep(0.5)
        print("You fall into a pit and get eaten by Goblins.")
        game_end()

def elf_game():
    print("You play a game.")
    time.sleep(0.3)
    print("The elf wants you to roll a dice with 6 sides.")
    print("If you roll an even number, you get to have dinner with the elf.")
    print("If you roll an odd number, he gets all of your stuff and you have to work in his mine.")
    game_end()

def dice_roll():
    roll = int(input("Roll a dice and enter the number."))
    if roll in [2,4,6]:
        print("You get to have dinner with the elf.")
        time.sleep(1)
        print("You eat some mushrooms.")
        time.sleep(1)
        print("You go onto a hell of a Trip and run into the forrest.")
        time.sleep(2)
        print("You pass out and get eaten by a pack of wolves.")
        game_end()
    else:
        print("He strips you and vanishes.")
        time.sleep(1)
        print("You freeze to death.")
        game_end()

def cave_selection():
    answer = ask_question("Do you want to enter the cave?", ["yes", "no"])
    if answer == "yes":
        print("You enter the cave.")
        time.sleep(1)
        print("You find a treasure chest.")
        time.sleep(1)
        print("You find a key.")
        time.sleep(1)
        print("You open the chest and find a golden sword.")
        time.sleep(1)
        print("You take the sword and go back into the forrest.")
    else:
        print("You continue on your way.")
        time.sleep(1)
        print("You go back into the forrest.")
        time.sleep(1)
        print("The ground is covered with leaves.")
        time.sleep(0.5)
        print("You fall into a pit and get eaten by Goblins.")
        game_end()

def ask_question(question, valid_answers):
    while True:
        answer = input(question).lower()
        if answer in valid_answers:
            return answer
        elif answer == "exit":
            game_end()
        else:
            print( "Invalid answer. If you want to exit enter 'exit' Otherwise please enter one of the following: " + ", ".join(valid_answers))

def game_end():
    answer = ask_question("Do you want to play again?", ["yes", "no"])
    if answer == "yes":
        game_initiation()
    else:
        print("Thanks for playing!")
        break



game_initiation()
