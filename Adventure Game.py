# 1. Nested Decisions: The Adventure Game 🏰
# Objective: To practice the use of nested if statements in creating a simple text-based adventure game.

# Task 1: Code Correction

# You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

# Buggy Code:
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You found a hidden treasure!")

# Task 2: Setting the Scene
# Based on the corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

if place == "cave":
    action = input("Do you want to light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("You found some sparkling gems!")
    else:
        print("You stumbled upon a map!")
        
# Task 3: Default Path
# If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.
        
if place == "forest":
    if action == "cross a river":
        action = input("Do you want to get in the boat or continue across the river? ")
        if action == "get in the boat":
            print("lets go down the river!")
        else:
            print("you found a fishing rod and caught some fish!")

else:
    pass

        
