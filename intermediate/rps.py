#!/usr/bin/env python

"""
File:   rps.py
Author: Tem Tamre

A rock-paper-scissors game against the CPU
Concepts covered: Random, IO, if/else, printing
"""

import random
import sys

def main():
    opponent = ai_guess()
    print("AI:", opponent)
    player = input("Choose one of [rock, paper, scissors]: ")[0].lower()
    while player not in "rps":
        player = input("Please choose one of [rock, paper, scissors]: ")[0].lower()

    if checkWin(player, opponent):
        print("Congratulations, you win!")
    elif player == opponent:
        print("You tied with the computer!")
    else:
        print("Sorry, the computer won.")


def ai_guess():
    option = random.randint(0,2)
    
    if option == 1:
        return "r"
    elif option == 2:
        return "p"
    elif option == 3:
        return "s"
    else:
        print("Error: Option was not one of [0, 1, 2]")
        exit()

def checkWin(p1, p2):
    rock =      (p1 == 'r') and (p2 == 's')
    paper =     (p1 == 'p') and (p2 == 'r')
    scissors =  (p1 == 's') and (p2 == 'p')

    return rock or paper or scissors

if __name__ == "__main__":
    main()