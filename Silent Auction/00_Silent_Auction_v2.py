"""
Silent Auction version 2
This is the second version of the base component
New function formatter added
"""


def main():
    auction_item = input("What is the auction for? ")
    reserve_price = number_checker("What is the reserve price? ")
    formatter("=", f"\nThe auction for the {auction_item} "
                   f"has started!\n")
    auction(reserve_price)


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def number_checker(question):
    ...


def auction(reserve):
    ...


# main program
main()