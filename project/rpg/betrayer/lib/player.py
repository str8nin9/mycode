#!/usr/bin/env python3
"""player class for rpg"""

import cmd
import textwrap
import sys
import os
import time
import random

#player setup
class player:
    def __init__(self):
        inventory = []
        print("success")
    name = input("name?\n>")
    p_hp = 20
#myplayer = player()

if __name__ == "__main__":
    hero = player()
    print(f"{player.name} has {player.p_hp} hp!")
    
    #print(player.hp)
