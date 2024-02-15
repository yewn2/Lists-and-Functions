def auction(reserve, item):
    highest = 0
    while highest >= 0:
        print(f"Highest bid: ${highest:.2f}")
        bid = float(input("Your bid: $"))
        while bid <= highest:
            if bid < 0:
                break
            print("Please enter a higher bid.")
            bid = float(input("Your bid: $"))
        if bid >= 0:
            highest = bid
        else:
            break
    if highest >= reserve:
        print(f"The auction for the {item} finished with a bid "
              f"of ${highest:.2f}")
    else:
        print(f"The {item} did not sell.")
