"""
Taxi Trips final version
"""


def main():
    driver = input("What is the driver's name? ")
    trips, tot_time, avg_time, income, avg_cost = trip()
    print("="*30)
    print(f"Driver {driver} had {trips} trips totalling {tot_time} minutes")
    print(f"The average time of all trips was {avg_time:.1f} minutes")
    print(f"The total income for the day was ${income:.2f}")
    print(f"The average cost of all trips was ${avg_cost:.2f}")


def trip():
    new_trip = True
    trips_taken = 0
    all_time = 0
    all_income = 0
    while new_trip:
        trips_taken += 1
        time_taken = float_checker("How many minutes did the trip take? ")
        cost = 10 + (time_taken * 2)
        print(f"This trip cost ${cost:.2f}")
        all_time += time_taken
        all_income += cost
        print()
        if input("Do you want to enter a new trip? Yes or No: ") == "Yes":
            new_trip = True
        else:
            new_trip = False
    average_cost = all_income / trips_taken
    average_time = all_time / trips_taken
    return trips_taken, all_time, average_time, all_income, average_cost


def float_checker(question):
    error = "\nSorry, you must enter a number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


# main program
main()