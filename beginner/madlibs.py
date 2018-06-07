#!/usr/bin/env python

"""
File: madlibs.py
Author: Tem Tamre

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"

def main():
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    vehicle = input("Enter the name of a vehicle: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    print("{name} went to visit their best friend at {place}. While he was there, he saw a {adverb} {verb} {vehicle} speeding down the road! While unsure of what was going on at first, {name} soon found out\
    that it was a street race!".format(name=name, place=place, vehicle=vehicle, verb=verb, adverb=adverb))

if __name__ == "__main__":
    main()
