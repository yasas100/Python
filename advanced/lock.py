#!/usr/bin/env python3

"""
File: lock.py
Name: Tem Tamre

Description
Concepts covered: Classes, assertion
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"


class ComboLock:
    def __init__(self, key1, key2, key3):
        self.key1 = key1
        self.key2 = key2
        self.key3 = key3
        self.dial = 0
        # self.attempt represents the current 3-number combination being
        # entered into the combination
        self.attempt = []
        # A left turn increments this by +1, a right turn decrements this by -1
        # If this value reaches +3 or -3, it means the lock was turned in
        # only one direction, so the lock won't open
        self.lefts = 0

    # Sets the dial at zero
    # Parameters: None
    # Return: None
    def reset(self):
        self.dial = 0
        self.lefts = 0

    # Turns the dial a number of ticks counter-clockwise and updates attempt
    # Parameter: ticks (number of ticks to move counter-clockwise)
    # Return: None
    def turn_left(self, ticks):
        self.dial -= ticks
        while self.dial < 0:
            self.dial += 60
        self.attempt.append(self.dial)
        if len(self.attempt) > 3:
            del self.attempt[0]
        self.lefts += 1

    # Turns the dial a number of ticks clockwise and updates attempt list
    # Parameter: ticks (number of ticks to move clockwise)
    # Return: None
    def turn_right(self, ticks):
        self.dial += ticks
        while self.dial > 59:
            self.dial -= 60
        self.attempt.append(self.dial)
        if len(self.attempt) > 3:
            del self.attempt[0]
        self.lefts -= 1

    # Returns true if the lock is open (attempt == keys), false otherwise
    # Parameters: None
    # Return: True if self.attempt == keys, false otherwise
    def isopen(self):
        return (self.attempt == [self.key1, self.key2, self.key3])\
               and (-3 < self.lefts < 3)

    # String representation of the ComboLock class
    # Parameter: None
    # Return: String representation of ComboLock
    def __repr__(self):
        return 'ComboLock({}, {}, {})'.format(self.key1, self.key2, self.key3)


# Do not modify these test functions
# However, you may write additional test functions
def test1():
    lock = ComboLock(25, 10, 0)
    assert str(lock) == 'ComboLock(25, 10, 0)' # __repr__ 
    assert not lock.isopen()
    
    # lock should open - basic
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()
       
    # lock should open - basic with reset in the middle
    lock.reset()
    lock.turn_right(35)
    lock.turn_left(5)
    lock.reset()
    lock.turn_right(25)
    lock.turn_left(15)
    lock.turn_right(50)
    assert lock.isopen()

    # lock should open - advanced 
    # the user turns the dial more than one full rotation
    lock.reset()
    lock.turn_right(85)
    lock.turn_left(135)
    lock.turn_right(50)
    assert lock.isopen()   
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_right(15)
    lock.turn_left(25)
    lock.turn_right(10)
    lock.turn_left(24)    
    assert not lock.isopen()
 
    
def test2():    
    lock = ComboLock(40, 30, 5)
    assert str(lock) == 'ComboLock(40, 30, 5)' 
    assert not lock.isopen()
    
    # lock should open 
    lock.reset()
    lock.turn_right(40)
    lock.turn_left(10)
    lock.turn_right(35)
    assert lock.isopen()
    
    # lock should not open - wrong combination
    lock.reset()
    lock.turn_left(20)
    lock.turn_left(10)
    lock.turn_left(25)    
    assert not lock.isopen()
    
 
def test():
    test1()
    test2()
    print("Passed all test cases")
    
if __name__ == "__main__":
    test()