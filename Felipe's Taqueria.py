TAQUERIA = {"Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00

}

def main():
    total = 0
    while True:
        try:
            # Prompt for input(Order until cotrol-d is entered).case insensitive and titlecased
            order = input("Item: ").lower().title()

            # Checking for exceptions(EOFErrors, and key errors)
        except EOFError:
            break
        except KeyError:
            pass
        if order not in TAQUERIA:
            pass
        else:
            # Updating the total price for each item on the menu
            total += TAQUERIA[order]

            # Display the total of all item lised thus far after every input
            print(f"${total:.2f}")

main()
