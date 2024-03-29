"""
Base component version 2
Integer checker function added
"""


def main():
    car_list = [[1, "Suzuki Van", 2], [2, "Toyota Corolla", 4],
                [3, "Honda CRV", 4], [4, "Suzuki Swift", 4],
                [5, "Mitsubishi Airtrek", 4], [6, "Nissan DC Ute", 4],
                [7, "Toyota Previa", 7], [8, "Toyota Hi Ace", 12],
                [9, "Toyota Hi Ace", 12]]
    car_list, booked_cars = book(car_list)
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
    ...


def end_program(lst):
    ...