CENTS_DENOMINATION = [50, 25, 10, 5]
def main():
    # Prompt user to insert a coin one at a time(convert input to integer)
    count = 0
    while True:
        try:
            user_prompt = int(input("Insert Coin: "))

            # Ignore any integer that isn't an accepted denomination
            if user_prompt in CENTS_DENOMINATION:
                count += user_prompt

                # Inform the user of the amount due after each coin is inserted to the machine
            if count < 50:
                    print(f"Amount Due: {50 - count}")

            # Output how many cent the user's owed
            if count >= 50:
                cents_owed = count - 50
                if count >= 50:
                    print(f"Change Owed: {cents_owed}")
                break
        except ValueError:
             print("That's not a valid integer.")
             if count == 50:
                  return cents_owed

main()
