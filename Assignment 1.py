#!/usr/bin/env python
# Assignment 1
"""
1. Ask the user three original questions and store their input as variables
2. Combine the three answers into a sentence of your choosing
3. Print out the final combined sentence using one of the string operations
4. Add docstrings and comments to your code
Stretch goal: Create a function that contains the print statement (pass the variables in as arguments to use in the print function).
"""

# get the user to input their name, hometown, and favorite football team
# store above as a variables
user_name = input("What's your name? ")
hometown = input("Where are you from? ")
football = input("What's your favorite football team? ")

# combine the answers into a sentence and print
info = "Hi, " + user_name + ", " + hometown + " is beatiful and " + football + " is a wonderful team."

def print_info():
    print(info)

print_info()

