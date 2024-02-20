"""
End Program version 1
Prints the vehicles booked at the end of the day
"""


def end_program(lst):
    print("VEHICLES BOOKED TODAY")
    for items in lst:
        vehicle_no = lst[0][0]
        vehicle = lst[0][1]
        person = lst[1]
        print(f"No. {vehicle_no} - {vehicle} - Booked by: {person}")
        lst.pop(0)
        lst.pop(0)
