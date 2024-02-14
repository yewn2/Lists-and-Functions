import sys


def pickUp(roll):
    name = input("What child would you like to pick up? ")
    for name in roll:
        while name not in roll:
            name = input("What child would you like to pick up? ")
        if name in roll:
            print("Your child: ")
            print("".join(name))
            print("is ready for pickup!")
            sys.exit()

