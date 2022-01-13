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
    def __init__(self, name, p_hp, ac):
        self.name = name
        self.p_hp = p_hp
        self.ac = ac
        #inventory = []
        #armor = {}
        #weapon = {}
    #modifiable health status
    def health(self):
        return self.p_hp

    def ac(self):
        return self.ac

    #def melee(self, opponent = 'none'):
        #attacks opponent
        #opponent = 

    

if __name__ == "__main__":
    name = input(">")
    p_hp = 20
    ac = 10
    hero = player(name, p_hp, ac)
    print(f"{hero.name} has {hero.p_hp} hp with an AC of {hero.ac}!")
    
    #print(player.hp)
