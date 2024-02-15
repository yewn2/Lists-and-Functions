def calcCost(roll):
    children_no = len(roll)
    hours = int(input("How many hours? "))
    cost = children_no * hours
    print(f"The cost of looking after {children_no} children for {hours} hours "
          f"is ${cost:.2f}")
