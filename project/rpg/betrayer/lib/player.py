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
    def __init__(self, name, p_hp):
        self.name = name
        self.p_hp = p_hp
        inventory = []
        print("success")
    #name = input("name?\n>")
    #p_hp = 20
#myplayer = player()

if __name__ == "__main__":
    name = input(">")
    p_hp = 20
    hero = player(name, p_hp)
    print(f"{hero.name} has {hero.p_hp} hp!")
    
    #print(player.hp)
