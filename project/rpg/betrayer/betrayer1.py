#!/usr/bin/python3
'''Author : Alonzo Harris RPG Game Highfantasy, low magic(for humans), horror?'''
#imports
import random
import dice
import requests

'''APis used listed here'''
dndurl = "https://www.dnd5eapi.co/api/"

'''lists and dictionaries'''
#add proper name of any WEAPON from dnd 5e armory will update with damage stats
weapons = ["club","dagger","longsword"]
#armory format example {club:1d4}
armory= {}

def beasts():
    #creates a beastiary
    monsters = ["goblin"]
    beastiary = {}
    #Beastiary = requests.get(f"{dndurl}/monsters").json()
    for monster in monsters:
        burl= f"{dndurl}/monsters/{monster}"
        beast= requests.get(burl).json()
        beastiary.update({monster: beast["hit_points"]})
def arms():
    #creates an armory
    weapons = ["club","dagger","longsword"]
    armory= {}
    for weapon in weapons:
    
        url= f"{dndurl}/equipment/{weapon}"
        x= requests.get(url).json()
        armory.update({weapon: x["damage"]["damage_dice"]})

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
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
      #for loot in rooms[currentRoom]['item']:
       #   i = 0
        #  print(f"You see a{rooms[currentRoom]['item'][i]}")
         # i += 1
    print("You found the following:")
    #seperates items on different lines
    print(*rooms[currentRoom]['item'], sep = "\n")
    #print(*f'You see a {rooms[currentRoom]["item"]}')
  print("---------------------------")

#an inventory, which is initially empty
inventory = []
get = ['get', 'take', 'Take', 'Get', 'pick up', 'Pick up', 'pickup', 'Pickup', 'obtain', 'Obtain'] 
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : ['key', 'longsword']
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : ['goblin'],
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : ['potion'],
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : ['cookie'],
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()
beasts()
arms()
#loop forever
while True:
    print(armory)
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
    if 'goblin' in rooms[currentRoom]['item'] and 'longsword' in inventory:
        print('A goblin is alarmed by your entrance! \n prepare for combat!!!')
        break
      ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'goblin' in rooms[currentRoom]['item']:
        print('A goblin has got you... GAME OVER!\n honestly, that is a pathetic way to die')
        quit()

fight = input('select from the following: attack, defend, Flee!')
if fight == 'attack':
    print('you deal' + dice.roll(armory['longsword']) + 'damage')
