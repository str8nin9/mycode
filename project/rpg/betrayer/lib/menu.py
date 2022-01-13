#!usr/bin/env python3
import room


'''persistent ingame menu'''
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
#inventory = []
#currentRoom = 'Hall'
room.room()
rooms = room.rooms
if __name__ == '__main__':
    showStatus()
