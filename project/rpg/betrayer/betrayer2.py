#!/usr/bin/python3
'''Author : Alonzo Harris RPG Game Highfantasy, low magic(for humans), horror?'''
#imports
import random
import dice
import requests
import cmd
import textwrap
import sys
import os
import time
#import all py files from lib directory
sys.path.insert(0, "/home/student/mycode/project/rpg/betrayer/lib")
import lib
import API
#import player
#import combat
'''lists and dictionaries'''
def showInstructions():
    #print a main menu and the commands
    #print(f"you have {player.player.self.hp} hit points")
    print('''
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print("You found the following:")
    #seperates items on different lines
    print(*rooms[currentRoom]['item'], sep = "\n")
    #print(*f'You see a {rooms[currentRoom]["item"]}')
  print("---------------------------")
API.arms()

API.beasts()
#an inventory, which is initially empty
inventory = []
get = ['get', 'take', 'Take', 'Get', 'pick up', 'Pick up', 'pickup', 'Pickup', 'obtain', 'Obtain'] 
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : ['key', 'longsword'],
                  #'mon' : [''],
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  #'item'  : ['z'],
                  'mon' : 'goblin',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion'],
                  #'mon' : [''],
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  #'mon' : [''],
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : ['cookie'],
                  #'mon' : [''],
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:
    #print(armory)
    showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
    move = ''
    while move == '':
        move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

  #if they type 'go' first
    if move[0] == 'go':
    #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
      #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

  #if they type 'get' first
    if move[0] in get:
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
            inventory += [move[1]]
        #display a helpful message
            print(move[1] + ' got!')
        #delete ONLY the taken item from the room
            rooms[currentRoom]['item'].remove(move[1])
        #otherwise, if the item isn't there to get
        else:
        #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
        
      ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        quit()
    if 'mon' in rooms[currentRoom] and 'longsword' in inventory:
        print(f'A {rooms[currentRoom]["mon"]} is alarmed by your entrance! \n prepare for combat!!!')
        break
      ## If a player enters a room with a monster
    elif 'mon' in rooms[currentRoom] and 'goblin' in rooms[currentRoom]['mon']:
        print(f'A {rooms[currentRoom]["mon"]} has got you... GAME OVER!\n honestly, that is a pathetic way to die')
        quit()

fight = input('select from the following: attack, defend, Flee!')
if fight == 'attack':
    print(f'you deal {dice.roll(API.armory["longsword"])} damage')
    
