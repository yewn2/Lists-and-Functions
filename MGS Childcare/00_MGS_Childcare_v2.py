def menu():
    choice = 0
    child_list = []
    while choice != 5:
        print("---------------------------------------------------------------"
              "--------")
        print("Welcome to MGS Childcare")
        print("What would you like to do? Please choose one of the items below")
        print("---------------------------------------------------------------"
              "--------")
        print()
        print("1 Drop off a child")
        print("2 Pick up a child")
        print("3 Calculate cost")
        print("4 Print roll")
        print("5 Exit the system")
        print()
        choice = int(input("Enter your choice (number between 1 and 5): "))
        print()
        if choice == 1:
            dropOff(child_list)
        elif choice == 2:
            pickUp()
        elif choice == 3:
            calcCost()
        elif choice == 4:
            printRoll()
        else:
            print("Goodbye")


def dropOff(roll):
    roll.append(input("What is your child's name? "))
    last_item = len(roll)
    second_to_last = last_item - 1
    child_name = roll[second_to_last:last_item]
    print()
    print("Your child: ")
    print("".join(child_name))
    print("has been added to the roll")
    print()
    return roll


def pickUp():
    ...


def calcCost():
    ...


def printRoll():
    ...


# main program
menu()
