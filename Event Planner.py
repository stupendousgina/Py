# 2. Quick Decisions: The Event Planner 🎉
# Objective: To practice the use of shorthand if statements in determining event-related decisions.

# Task 1: Code Correction
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.

audio_visual = "audio system" if attendees >= 100 else "projector"
print(audio_visual)

# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

veg = input("Would you like vegetarian food? (yes/no) ")
meal = "Veggie Delight Caterers" if veg == "yes" else "Gourmet Meals Caterers"
print(meal)



