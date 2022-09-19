from gavel import logo
import os

print(logo)

users_dictionary = {}

def kill_switch(switch):
    if switch == 'yes':
        os.system('clear')
    else:
        print(users_dictionary)
        find_highest_bid()
        exit()

def find_highest_bid():
    for key in users_dictionary:
        if users_dictionary[key]:
            exit()
        

while True:
    name = input("Bidder's Name: ")
    bid = float(input("What's your bid: "))
    users_dictionary[name] = bid
    switch = input("Are there other bidder (yes/no)? ")
    kill_switch(switch)
    