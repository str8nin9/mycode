#!/usr/bin/env python3
    #This is a guess the object game using items from a class room
#from time import sleep
correct = "head"
guess = ""
round = 0
name = input("enter name: ").capitalize()
input("Waking up, you feel sore and dizzy.(press enter to continue through text)") #; sleep(2)
input("You feel a damp coldnesss emanating from the back of your head") #; sleep(6)
input("You wince in pain as you touch the back of your head, viewing your hand you are horrified by the amount of blood that cakes it.") #; sleep(10)
input("You remember turning your back to youir teacher after refusing to do a dumb pop quiz in class")#; sleep(6)
input("Hidden in this class room is an object that contains the key to the door, find it before you bleed out!!")#; sleep(6)
while guess != correct:
    round += 1
    guess = input("Take a stab at it: ").lower()
    if guess != correct and round == 1:
        input("Awwww, Poor, stupd " + name + " let me give you a hint")
        input("Without it, attending class is pointless")
    elif guess in ("body", "me") and round != 8:
        input("so an old dog can learn? close but not quite")
    elif guess != correct and round == 2:
        input("you put knowledge in it")
    elif guess != correct and round == 3:
        input("it is the most annoying thing in the room")
    elif guess != correct and round == 4:
        input("it is round and apparently empty")
    elif guess != correct and round == 5:
        input("it has 5 holes")
    elif guess != correct and round == 6:
        input("it is leaking...")
    elif guess != correct and round == 7:
        input("as your vision fades to black you hear the voice say \"apparently it is also an idiot\".....")
        break
    elif guess == correct:
        print("That's right it is in YOUR " + correct.upper() +"!!! *cackling*")
if guess != correct:
    input("YOU DIED")
else:
    input("you find the key in you skull and in desperation tug! instantly killing you because you are not a medical professional and should not be digging around in your head.")
    input("YOU DIED")
