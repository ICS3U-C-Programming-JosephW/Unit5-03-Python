#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 12, 2025
# This program calculates the middle
# percentage of a level entered by
# the user, based on
# https://en.wikipedia.org/wiki/Academic_grading_in_Canada#Ontario.


# Define a function to calculate the
# middle percentage.
def calc_mark(level):
    # Initialize the mark to 0
    # to use it later.
    mark = 0

    # Check if the level entered by
    # the user was a 4+.
    if level == "4+":
        # Set the mark to 98.
        mark = 98
    # Otherwise, check if the level
    # entered was a 4.
    elif level == "4":
        # Set the mark to 91.
        mark = 91
    # Otherwise, check if the level
    # entered was a 4-.
    elif level == "4-":
        # Set the mark to 83.
        mark = 83
    # Otherwise, check if the level
    # entered was a 3+.
    elif level == "3+":
        # Set the mark to 78.
        mark = 78
    # Otherwise, check if the level
    # entered was a 3.
    elif level == "3":
        # Set the mark to 75.
        mark = 75
    # Otherwise, check if the level
    # entered was a 3-.
    elif level == "3-":
        # Set the mark to 71.
        mark = 71
    # Otherwise, check if the level
    # entered was a 2+.
    elif level == "2+":
        # Set the mark to 68.
        mark = 68
    # Otherwise, check if the level
    # entered was a 2.
    elif level == "2":
        # Set the mark to 65.
        mark = 65
    # Otherwise, check if the level
    # entered was a 2-.
    elif level == "2-":
        # Set the mark to 61.
        mark = 61
    # Otherwise, check if the level
    # entered was a 1+.
    elif level == "1+":
        # Set the mark to 58.
        mark = 58
    # Otherwise, check if the level
    # entered was a 1.
    elif level == "1":
        # Set the mark to 55.
        mark = 55
    # Otherwise, check if the level
    # entered was a 1-.
    elif level == "1-":
        # Set the mark to 51.
        mark = 51
    # Otherwise, check if the level
    # entered was a 0.
    elif level == "0":
        # Set the mark to 25.
        mark = 25
    # Otherwise, the level entered
    # was not valid.
    else:
        # Set the mark to -1 to
        # indicate it is invalid.
        mark = -1

    # Return the resulting mark
    # to be used for display.
    return mark


# Define the main function.
def main():
    # Get the level input from the user.
    user_level = input("\nEnter the level you want converted to a percentage: ")

    # Assign the middle percentage to
    # the mark calculator function to
    # get its return value.
    middle_percentage = calc_mark(user_level)

    # Check if the user entered an invalid level.
    if middle_percentage == -1:
        # Display that their level is not valid.
        print(f"\n{user_level} is not a valid level.")
    # Otherwise, they entered a valid level.
    else:
        # Display the resulting middle
        # percentage to the user.
        print(f"\nLevel {user_level} has a middle percentage of {middle_percentage}%.")


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main function if so.
    main()
