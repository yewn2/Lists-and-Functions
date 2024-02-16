"""
Trip function v1
"""


def trip():
    new_trip = True
    trips_taken = 0
    all_time = 0
    all_income = 0
    while new_trip:
        trips_taken += 1
        time_taken = float(input("How many minutes did the trip take? "))
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
