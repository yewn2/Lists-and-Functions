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
        choice = number_checker("Enter your choice (number between 1 and 5): ")
        print()
        if choice == 1:
            child_list = dropOff(child_list)
        elif choice == 2:
            pickUp(child_list)
        elif choice == 3:
            calcCost(child_list)
        elif choice == 4:
            printRoll(child_list)
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


def pickUp(roll):
    name = str(input("What child would you like to pick up? "))
    number_names = len(roll)
    one_before = number_names - 1
    for i in roll:
        while name not in roll[one_before:number_names]:
            number_names -= 1
            one_before -= 1
            if number_names == 0:
                break
        if name in roll[one_before:number_names]:
            print(f"\nYour child {name} is ready for pickup!\n")
            break
        else:
            print(f"Your child {name} is not present; please try again.\n")
            break
            

def calcCost(roll):
    children_no = len(roll)
    hours = number_checker("How many hours? ")
    cost = children_no * hours
    print(f"The cost of looking after {children_no} children for {hours} hours "
          f"is ${cost:.2f}")


def printRoll(roll):
    print(", ".join(roll))


def number_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


# main program
menu()
