def room():
    global rooms
    rooms = {

                'Hall' : {
                      'south' : 'Kitchen',
                      'east'  : 'Dining Room',
                      'item'  : ['key', 'longsword'],
                      #'mon' : [''],
                      'desc' : 'you step into an old decrepit Hall \n in the past you could imagine great balls being held here. but now it lies in ruin'
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
