#!/usr/bin/env python3

"""
File: bank.py
Name: Tem Tamre

Bank account simulation to learn how to use classes in Python
Concepts covered: Classes

Base:       deposit, withdraw, view account
Extension:  (1) chequing/savings (2) savings growth (3) transaction history
"""

__author__      = "Tem Tamre"
__copyright__   = "ttamre@ualberta.ca"


class BankAccount:
    def __init__(self, name, balance=5000):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def showAccount(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


class BankAccount2:  # BankAccount with extensions
    def __init__(self, name, chequing=1000, savings=5000):
            self.name = name
            self.chequing = chequing
            self.savings = savings
            self.history = ["Created account for {} with ${} in chequing and ${} in savings"]
        
    def deposit(self, account, amount):
        if account.lower()[0] == "c":
            self.chequing += amount
            self.history.append("Deposited ${} into chequing".format(amount))
        elif account.lower()[0] == "s":
            self.savings += amount
            self.history.append("Deposited ${} into savings".format(amount))
        else:
            print("Error: Account not recognized")

    def withdraw(self, account, amount):
        if account.lower()[0] == "c":
            self.chequing -= amount
            self.history.append("Withdrew ${} from chequing".format(amount))
        elif account.lower()[0] == "s":
            self.savings -= amount
            self.history.append("Withdrew ${} from savings".format(amount))
        else:
            print("Error: Account not recognized")
    
    def showAccount(self):
        print("Name:", self.name)
        print("Chequing:", self.chequing)
        print("Savings:", self.savings)

    def transaction_history(self):
        print("--- Transaction History ---")
        for action in self.history:
            print(action)
    
    def growth(self):
        self.savings *= 1.02
        print("Savings account grew to ${}".format(self.savings))


def test1():
    alex  = BankAccount("Alex")
    bobby = BankAccount("Bobby", 3250)

    # Testing Alex
    assert alex.name == "Alex"
    assert alex.balance == 5000
    alex.deposit(500)
    alex.deposit(1500)
    alex.withdraw(250.25)
    assert alex.balance == 6750.75
    alex.showAccount()

    # Testing Bobby
    assert alex.name == "Bobby"
    assert alex.balance == 3250
    alex.deposit(alex.balance)
    alex.withdraw(500)
    alex.withdraw(1250.50)
    assert alex.balance == 4749.5
    alex.showAccount()


def test2():
    chris = BankAccount2("Chris")
    dave  = BankAccount2("Dave", 1500, 10000)

    # Testing Chris
    assert chris.name == "Chris"
    assert chris.chequing == 1000
    assert chris.savings == 5000
    chris.deposit("c", 200)
    chris.deposit("c", 500)
    chris.deposit("s", 5000)
    chris.growth()
    assert chris.chequing == 1700
    assert chris.savings == 10200

    # Testing David
    assert dave.name == "Dave"
    assert dave.chequing == 1500
    assert dave.savings == 10000
    dave.deposit("c", 200)
    dave.deposit("s", 5000)
    dave.withdraw("s", 3250)
    assert dave.chequing == 1700
    assert dave.savings == 11750
    dave.growth()
    dave.transaction_history()
    assert dave.savings == 11985


if __name__ == "__main__":
    test1()
    test2()
    print("Program success!")