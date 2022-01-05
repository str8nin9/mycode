#!/usr/bin/env python3

def main():
    #global nums
    #global words
    nums= [1,2,3,4,5]
    words= {"verb": "sprint",
            "adjective": "awesome",
            "noun": "Python"}

    name = input("What is your name?\n>").capitalize
    
    # Hi <name>! Welcome to Day 2 of Python Training!
    #print("Hi " + name + "! Welcome to Day ", nums[1] + " of " + words["noun"] + " Training!")
    print("Hi " + name + "! Welcome to Day {} of {}  Training!".format(nums[1],words["noun"]))

main()
