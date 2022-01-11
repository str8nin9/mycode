
import dice
import requests


dndurl = "https://www.dnd5eapi.co/api"
#beasriary
monsters = requests.get(f"{dndurl}/monsters").json()

#items
items = requests.get(f"{dndurl}/equipment").json()

weapons = ["club","dagger","longsword"]
armory= {}
for weapon in weapons:
    url= f"{dndurl}/equipment/{weapon}"
    x= requests.get(url).json()
    armory.update({weapon: x["damage"]["damage_dice"]})
    #print(armory)


if __name__ == "__main__":
    #for name in items['results']:
    print(armory)
    
        
