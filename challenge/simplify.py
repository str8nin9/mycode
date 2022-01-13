#!/usr/bin/env python3

import pandas as pd

def menu():
    """this will print out a menu of choices so the user knows what is available."""
    #while True:
    demolist = ["Apple","Banana","Cherries","Dragonfruit"]
    list_length = len(demolist)
    for i in range(list_length):
        print(f'{i+1}: {demolist[i]}')
      # print("Choose a fruit: ")
          
    while True:
        choice = input(">")
        choice = int(choice)
        choice -= 1
        if demolist[choice] in demolist:
            print(f'You picked {demolist[choice]}')
        else:
            print("That was not an option.")
            break

def sports():
    """what is a more efficient way to return this info instead of using a bunch
    of if/elif/else lines?"""

    while True:

        quitwords= ["Q", "q", "Quit", "quit", "Stop", "stop", "End", "end"]

        print("\nPick a sport to see what equipment you need!")
        print(["football", "soccer", "tennis", "baseball"])

        sport= input("\n>")

        if sport in quitwords:
            break

        if sport == "football":
            print("football, pads, helmet")
            break

        elif sport == "soccer":
            print("soccer ball, shin guards")
            break

        elif sport == "tennis":
            print("two tennis rackets, tennis ball")
            break

        elif sport == "baseball":
            print("baseball, bat, glove")
            break

        else:
            print("That is not one of the correct sports!")


def creation():
    poke_df = pd.read_csv("pokedex.txt", index_col=1)
    stat = input('pick one: attack, defense, HP:\n>').capitalize
    print(f"\n10 best {stat}:")
    print(poke_df.sort_values([{stat}], ascending = False).head(10))
   


def challenge():
    # HARDER THAN IT LOOKS:
    # I have a bunch of numbers that I need to increase by 1!
    nums = [5,10,15,20,25]
    # this will cause an error! how should we do this, then?
    list_length = len(nums)
    for i in range(list_length):
        nums[i] += 1
    print(nums) 
#menu()
# sports()
#creation()
challenge()
