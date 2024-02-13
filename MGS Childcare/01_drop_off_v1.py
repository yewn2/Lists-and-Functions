def dropOff(roll):
    roll.append(input("What is your child's name? "))
    print(f"{roll[:1]} has been added to the roll.")
    return roll


child_list = []

dropOff(child_list)
