#!/usr/bin/env python3
import requests

dndurl = "https://www.dnd5eapi.co/api/"

def beasts():
    #creates a beastiary
    monsters = ["goblin"]
    global beastiary
    beastiary = {}
    #Beastiary = requests.get(f"{dndurl}/monsters").json()
    for monster in monsters:
        burl= f"{dndurl}/monsters/{monster}"
        beast= requests.get(burl).json()
        beastiary.update({monster: beast["hit_points"]})
def arms():
    #creates an armory
    #add proper name of any WEAPON from dnd 5e armory will update with damage stats
    weapons = ["club","dagger","longsword"]
    global armory
    armory= {}
    for weapon in weapons:
    
        url= f"{dndurl}/equipment/{weapon}"
        x= requests.get(url).json()
        armory.update({weapon: x["damage"]["damage_dice"]})
if __name__ == "__main__":
    arms()
    beasts()
    print(armory)
    print(beastiary)
