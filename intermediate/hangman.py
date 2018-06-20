#!/usr/bin/env python3

"""
File:   hangman.py 
Author: Tem Tamre

A python implementation of hangman
Concepts covered: Strings, if/else, while, functions
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"

import random
import sys

def main():
    lives = 5
    index = random.randint(0,9)
    possible_words = ["awkward", "bagpipes", "burglar", "hyper", "magical", "oxygen", "pajamas", "trapped", "wilderness", "zombie"]
    selected_word = possible_words[index]
    guessed_letters = []

    print("The answer is a {} letter word ({})".format(len(selected_word), selected_word))
    while(lives > 0):
        checkWin(guessed_letters, selected_word)
        print("You have {} lives remaining.".format(lives))
        letter = input("Guess a letter: ")[0].lower()
        guessed_letters.append(letter)

        if letter in selected_word:
            print("Correct!")
            for i in range(len(selected_word)):
                if selected_word[i] in guessed_letters:
                    print(selected_word[i], end=" ")
                else:
                    print("_", end=" ")
            print()
        else:
            print("Incorrect")
            lives -= 1
    
    # This section will only execute if you lose
    print("You ran out of lives.")
    exit()
        
def checkWin(guessed_letters, selected_word):
    if set(guessed_letters) == set(selected_word):
        print("You won! Congratulations!")
        exit()

if __name__ == "__main__":
    main()