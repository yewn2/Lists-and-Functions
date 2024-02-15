def auction(reserve):
    highest = 0
    while highest >= 0:
        print(f"Highest bid: ${highest:.2f}")
        highest = float(input("Your bid: $"))
    if highest >= reserve:
        return True
