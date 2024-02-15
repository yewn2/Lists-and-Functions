"""
Silent Auction final version
"""


def main():
    auction_item = input("What is the auction for? ")
    reserve_price = number_checker("What is the reserve price? ")
    print(formatter("=", f"\nThe auction for the {auction_item} "
                         f"has started!\nEnter '-1' to end the auction"))
    auction(reserve_price, auction_item)


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def number_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


def auction(reserve, item):
    highest = 0
    while highest >= 0:
        print(f"Highest bid: ${highest:.2f}")
        bid = number_checker("Your bid: $")
        while bid <= highest:
            if bid < 0:
                break
            print("Please enter a higher bid.")
            bid = number_checker("Your bid: $")
        if bid >= 0:
            highest = bid
        else:
            break
    if highest >= reserve:
        print(formatter("|", f"The auction for the {item} "
                             f"finished with a bid of ${highest:.2f}"))
    else:
        print(formatter("/", f"The {item} did not sell."))


# main program
main()
