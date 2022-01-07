#!/usr/bin/env python3
"""Number guessing game!"""

import random

esc = ["q", "Q", "quit", "Quit", "exit", "Exit"]

def main():
    num= random.randint(1,100)

    while True:
        try:
            guess= int(input("Guess a number between 1 and 100: \n >"))
            if guess > num:
                print("Too high!")

            elif guess < num:
                print("Too low!")

            else:
                print("Correct!")
                break
        except ValueError:
            es = input("please enter a number!~ or press q to quit")

            if es in esc:
                break
           
main()
