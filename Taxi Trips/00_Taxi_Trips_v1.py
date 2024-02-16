"""
Taxi Trips version 1
This is the first version of the base component
No functions except main are written yet
"""


def main():
    driver = input("What is the driver's name? ")
    trips, tot_time, avg_time, income, avg_cost = trip(driver)
    print("="*30)
    print(f"Driver {driver} had {trips} trips totalling {tot_time} minutes")
    print(f"The average time of all trips was {avg_time:.1f} minutes")
    print(f"The total income for the day was ${income:.2f}")
    print(f"The average cost of all trips was ${avg_cost:.2f}")


def trip(name):
    ...


def float_checker(question):
    ...
