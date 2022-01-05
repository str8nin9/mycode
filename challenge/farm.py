#!/usr/bin/env python3

#dictionary farms is 3 dictionaries assigned ele NE-0 W-1 SE-2
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

veg = ["carrots", "celery"]

#definitions
def meat():
    for farm in farms:
        if farm["name"].upper() == choice.upper():
            for product in farm["agriculture"]:
                if product not in veg:
                    print(product)
def vegs():    
    if farm["name"].upper() == choice.upper():
        for product in farm["agriculture"]:
            print(product)
#select your farm!!!
#print("select from the following:")
#for farm in farms:
 #   print( farm )
#choice = input(": ").upper

selection = input("select a farm from the following:\n NE \n W \n SE \n type here: ").upper()
choice = selection + " Farm"

#dietary needs

diet = input("do you want veggies? \n (y/n): ").lower()

#runing functions
if diet == "y":
    print("-------------------LIST---------------------")
    vegs()
if diet == "n":
    print("-------------------LIST---------------------")
    meat()
else: 
    print("error")


