#!/usr/bin/env python3
char_name = input("hich character do you want to know about? (Flash, Batman, Superman): ").lower()
char_stat = input( "What statistic do you want to know about? (strength, speed, or intelligence): ").lower()

bank = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lost"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

print(f"{char_name.capitalize()}'s {char_stat} is the {bank[char_name][char_stat]}") 

