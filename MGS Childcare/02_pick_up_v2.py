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


child_list = ["Raf", "Robson", "Alex"]

pickUp(child_list)
