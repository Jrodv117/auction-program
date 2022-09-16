from gavel import logo
import os

print(logo)

users_dictionary = {}

def kill_switch(switch):
    if switch == 'yes':
        os.system('clear')
    else:
        print(users_dictionary)
        exit()

while True:
    name = input("Bidder's Name: ")
    bid = float(input("What's your bid: "))
    users_dictionary[name] = bid
    switch = input("Are there other bidder (yes/no)? ")
    kill_switch(switch)
    