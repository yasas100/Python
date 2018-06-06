#!/usr/bin/env python

"""
hangman.py - A python implementation of hangman

Concepts covered: Strings, if/else, while, functions
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"

import sys

def main():
    lives = 5
    index = random.randint(0,9)
    possible_words = ["Awkward", "Bagpipes", "Burglar", "Hyper", "Magical", "Oxygen", "Pajamas", "Trapped", "Wilderness", "Zombie"]
    selected_word = possible_words[index]
    guessed_letters = []

    print("The answer is a {} letter word".format(len(selected_word)))
    while(lives > 0):
        checkWin()
        print("You have {} lives remaining.".format(lives))
        guessed_letters.append(input("Guess a letter: "))
        if letter in selected_word:
            print("Correct!")
            for i in range(len(selected_word)):
                if selected_word[i] in guessed_letters:
                    print(selected_word[i])
                else:
                    print("_")
        else:
            print("Incorrect")
            lives -= 1
    
    # This section will only execute if you lose
    print("You ran out of lives.")
    exit()
        
def checkWin():
    if set(guessed_letters) == set(selected_word):
        print("You won! Congratulations!")
        exit()