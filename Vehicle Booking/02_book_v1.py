"""
Booking function version 1
Asks for seats needed
Displays cars available including those with not enough seats
Checks name of user and returns it
"""


def book(lst):
    taken = []
    seats = int(input("Please enter the number of seats required "
                      "(Type -1 to quit): "))
    while seats >= 0:
        print("VEHICLE NUMBER - TYPE - NO. SEATS")
        for cars in lst:
            if cars[2] < seats:
                print(f"No. {cars[0]} - {cars[1]} - {cars[2]} - NOTE: "
                      f"Car does not have enough seats")
            else:
                print(f"No. {cars[0]} - {cars[1]} - {cars[2]}")
        print()
        car_no = int(input("Enter a number to book: "))
        taker = input("Enter your name: ")
        taken.append(lst[(car_no - 1)][0:2])
        taken.append(taker)
        print(f"{lst[(car_no - 1)][1]} booked by {taker}")
        lst.pop((car_no - 1))
        print()
        seats = int(input("Please enter the number of seats required "
                          "(Type -1 to quit): "))
        print()
    return taken
