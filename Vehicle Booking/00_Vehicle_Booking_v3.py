"""
Base component version 3
Car booking function added
"""


def main():
    car_list = [[1, "Suzuki Van", 2], [2, "Toyota Corolla", 4],
                [3, "Honda CRV", 4], [4, "Suzuki Swift", 4],
                [5, "Mitsubishi Airtrek", 4], [6, "Nissan DC Ute", 4],
                [7, "Toyota Previa", 7], [8, "Toyota Hi Ace", 12],
                [9, "Toyota Hi Ace", 12]]
    booked_cars = book(car_list)
    end_program(booked_cars)


def int_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


def book(lst):
    taken = []
    seats = int_checker("Please enter the number of seats required "
                        "(Type -1 to quit): ")
    while seats >= 0:
        print("VEHICLE NUMBER - TYPE - NO. SEATS")
        for cars in lst:
            if cars[2] < seats:
                print(f"No. {cars[0]} - {cars[1]} - {cars[2]} - NOTE: "
                      f"Car does not have enough seats")
            else:
                print(f"No. {cars[0]} - {cars[1]} - {cars[2]}")
        print()
        car_no = int_checker("Enter a number to book: ")
        taker = input("Enter your name: ")
        taken.append(lst[(car_no - 1)][0:2])
        taken.append(taker)
        print(f"{lst[(car_no - 1)][1]} booked by {taker}")
        lst.pop((car_no - 1))
        print()
        seats = int_checker("Please enter the number of seats required "
                            "(Type -1 to quit): ")
        print()
    return taken


def end_program(lst):
    ...
