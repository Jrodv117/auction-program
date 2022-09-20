import os
from gavel import logo

print(logo)

users_dictionary = {}


def kill_switch(flag):
    """kills code when user chooses to exit"""
    if flag == "yes":
        os.system("clear")
    else:
        print(users_dictionary)
        find_highest_bid()
        exit()


def find_highest_bid():
    """finds the highest bid and bidder"""
    highest_bidder = max(users_dictionary, key=users_dictionary.get)
    highest_bid = int((max(users_dictionary.values())))
    print(f"The winning bidder is: {highest_bidder} with a bid of: ${highest_bid}")


def main():
    """main function that is the point of execution"""
    while True:
        name = input("Bidder's Name: ")
        bid = float(input("What's your bid: "))
        users_dictionary[name] = bid
        switch = input("Are there other bidder (yes/no)? ")
        kill_switch(switch)


if __name__ == "__main__":
    main()
