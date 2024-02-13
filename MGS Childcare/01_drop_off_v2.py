def dropOff(roll):
    roll.append(input("What is your child's name? "))
    last_item = len(roll)
    second_to_last = last_item - 1
    child_name = roll[second_to_last:last_item]
    print("Your child: ")
    print("".join(child_name))
    print("has been added to the roll")
    return roll


child_list = []


# main program
child_list = dropOff(child_list)
