#!/usr/bin/env python

"""
guess.py - A number guessing game

Concepts covered: Random, IO, if/else, printing
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"

import random

# Extensions: Input validation, lives, user-determined max number
def main():
    answer = random.randint(1,10)
    response = int(input("Enter a number between 1 and 10: "))

    if answer == repsonse:
        print("Correct! You win!")
    else:
        print("Incorrect, sorry.")

if __name__ == "__main__":
    main()