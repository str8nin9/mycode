#!usr/bin/env python3

#add rooms to the function
def room():
    global rooms
    #when adding descriptions use 'desc' : ''' multi line string '''
    rooms = {

                'Hall' : {
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : ['key', 'longsword'],
                      #'mon' : [],
                      'desc' : '''you step into an old decrepit Hall
in the past you could imagine great balls
being held here. but now it lies in ruin'''
                    },

                'Kitchen' : {
                      'north' : 'Hall',
                      #'item'  : ['z'],
                      'mon' : 'goblin',
                      'desc' : ' ',
                    },
                'Dining Room' : {
                      'west' : 'Hall',
                      'south': 'Garden',
                      'item' : ['potion'],
                      #'mon' : [''],
                      'north' : 'Pantry',
                      'desc' : ' ',
                   },
                'Garden' : {
                      'north' : 'Dining Room',
                      #'mon' : [''],
                      'desc' : ' ',
                   },
                'Pantry' : {
                      'south' : 'Dining Room',
                      'item' : ['cookie'],
                      #'mon' : [''],
                      'desc' : ' ',
                }
             }
if  __name__ == "__main__":
    room()
    print(rooms)
