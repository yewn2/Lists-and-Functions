"""
Arrest warrant version 1
This component checks the name of the speeder and checks if they have an arrest
warrant placed out for them
"""


def arrest(name):
    name2 = name.lower()
    if (name2 == "james wilson" or name2 == "helga norman"
            or name2 == "zachary conroy"):
        print(f"{name.upper()} - WARRANT TO ARREST")
