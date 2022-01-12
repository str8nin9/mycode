#!/usr/bin/env python3
"""player class for rpg"""

import cmd
import textwrap
import sys
import os
import time
import random
import dice

#player setup
class player:
    def __init__(self, name, p_hp):
        global inventory
        global weapon
        global armor
        self.name = name
        self.p_hp = p_hp
        #inventory = []
        #armor = {}
        #weapon = {}
    #modifiable health status
    def health(self):
        return self.p_hp

    def ac(self):
        return 10

    #def melee(self, opponent = 'none'):
        #attacks opponent
        #opponent = 

    

if __name__ == "__main__":
    name = input(">")
    p_hp = 20
    hero = player(name, p_hp)
    print(f"{hero.name} has {hero.p_hp} hp!")
    
    #print(player.hp)
