import random

def main():
    # Prompt user for a level, n. If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))

            # Checking for positive integer
            if level < 1:
                continue

        # Checking for Non integer value
        except ValueError:
            pass
        else:
            break

    # Randomly generates an integer between 1 and n, inclusive, using the random module.
    rand_num = random.randint(1, level)

    # Prompt user for a guess integer. If the guess is not a positive integer, the program should prompt the user again.
    while True:
        try:
            guess = int(input("Guess: "))
            if guess == rand_num:
                print("Just right!")
                return
            elif guess < 1:
                pass
            # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
            elif guess < rand_num:
                print("Too small!")
            # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
            elif guess > rand_num:
                print("Too Large!")
            # If the guess is the same as that integer, the program should output Just right! and exit.
        except ValueError:
            pass

main()
