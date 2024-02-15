"""
Silent Auction version 1
This is the first version of the base component
No functions except main are written yet
"""


def main():
    auction_item = input("What is the auction for? ")
    reserve_price = number_checker("What is the reserve price? ")
    formatter("=", f"\nThe auction for the {auction_item} "
                   f"has started!\n")
    auction(reserve_price)


def formatter(symbol, text):
    ...


def number_checker(question):
    ...


def auction(reserve):
    ...


# main program
main()