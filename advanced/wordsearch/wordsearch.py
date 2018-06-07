#!/usr/bin/env python

"""
File:   wordsearch.py
Author: Tem Tamre

Basic terminal wordsearch game
Concepts covered: Classes, 2D lists, file IO

Sources:
https://stackoverflow.com/questions/3739909/how-to-strip-all-whitespace-from-string

BUG: Rows are printing in all columns
"""

from random import *
import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def main():
    cw = Crossword()
    cw.generate_crossword()
    cw.print_grid()
	
class Crossword:
    def __init__(self, filename="wordlist.txt"):
        self.length = 10
        self.width  = 10
        self.grid   = [["."] * 10] * 10

        self.hCount = 2
        self.vCount = 2
        self.dCount = 2

        self.wordlist = self.getWords(filename)
        self.included_words = []
        self.errorCheck()

    # Return: The crossword puzzle to be used
    def generate_crossword(self):
        # Insert all the words to be used in their proper orientations
        self.insert_horizontal()
        #self.insert_vertical()
        #self.insert_diagonal()

        # Fill the rest
        for i in range(self.length):
            for j in range(self.width):
                if self.grid[i][j] == ".":
                    randIndex = randint(0,25)
                    self.grid[i][j] = str(i) + str(j)

    def insert_horizontal(self):
        for i in range(self.hCount):
            word = self.wordlist.pop()
            self.included_words.append(word)
            x = randint(0,10-len(word))
            y = randint(0,9)

            print(word, x, y, end="\n\n")
            for letter in word:
                self.grid[y][x] = letter.upper()
                x += 1
        

    def insert_vertical(self):
        for i in range(self.vCount):
            word = self.wordlist.pop()
            self.included_words.append(word)
            x = randint(0,9)
            y = randint(0,10-len(word))

            for letter in word:
                self.grid[y][x] = letter.upper()
                y += 1

    def insert_diagonal(self):
        for i in range(self.dCount):
            word = self.wordlist.pop()
            self.included_words.append(word)
            x = randint(0,10-len(word))
            y = randint(0,10-len(word))

            for letter in word:
                self.grid[y][x] = letter.upper()
                x += 1
                y += 1

    # Return: words to be used in the wordsearch, sorted randomly
    # Parameters: filename (string, path to the wordsearch text file)
    def getWords(self, filename):
        f = open(filename)
        wordlist = []

        for line in f.readlines():
            wordlist.append("".join(line.split()))

        f.close()
        shuffle(wordlist)
        return wordlist

    # Prints the grid in it's current state
    def print_grid(self):
        for i in range(self.length):
            for j in range(self.width):
                print(self.grid[i][j], end=" ")
            print()

    def errorCheck(self):
        # Make sure the horzontal/vertical/diagonal word counts don't exceed the amount of words in the wordlist
        a = self.hCount + self.vCount + self.dCount
        b = len(self.wordlist)
        try: assert((self.hCount + self.vCount + self.dCount) < len(self.wordlist))
        except AssertionError:
            print("ERROR: Wordcounts exceed the length of the word list ({} > {})".format(a, b))
            exit(1)

if __name__ == "__main__":
	main()