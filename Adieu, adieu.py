import inflect
engine = inflect.engine()

def main():
    # Initialize an empty list that would be updated with imput of user's name
    names = []
    # Prompt for name, one per line till ctrl-d
    while True:
        try:
            name = input("Name: ").capitalize()

            # Update empty list
            names.append(name)

        except EOFError:
            break

    # Call inflect on names inputted by user
    Names = engine.join(names)

    # Print output
    print(f"\nAdieu, adieu, to {Names}")

main()
