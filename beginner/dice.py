#!/usr/bin/env python

"""
dice.py - Rolls a dice and outputs the result

Concepts covered: Random, printing
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"

import random

def main():
    input("Press any button to roll the dice ")
    
    roll = random.randint(1,6)
    print("You rolled a " + str(roll) + "!")

if __name__ == "__main__":
    main()