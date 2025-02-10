import random


def main():
    # Counter for while loop
    count = 0

    # A counter that tracks correct answers
    correct_answer = 0

    # A counter to keep track of wrong answers
    incorrect = 0

    # Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again
    level = get_level()

    # Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
# digits.
    while count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        maths = x + y

        # Prompts the user to solve each of those problems
        i = 0
        for i in range(3):
            try:
                solve_maths = int(input(f"{x} + {y} = "))
            except ValueError:
                pass

            if solve_maths == maths:
                correct_answer += 1
                break

            # The program should output EEE and prompt the user again
            if not solve_maths == maths:
                incorrect += 1
                print("EEE")

        if incorrect == 3:
            print(f"{x} + {y} = {maths}")

        count += 1
        incorrect = 0

    # The program should ultimately output the user’s score: the number of correct answers out of 10.
    print(f"Score: {correct_answer}")


# Definition of get_level
def get_level():
    lev = 0
    while True:
        try:
            lev = int(input("Level: "))
        except ValueError:
            pass

        if lev != 1 and lev != 2 and lev != 3:
                pass

        if lev == 1 or lev == 2 or lev == 3:
            return lev

# Define generate_integer


def generate_integer(level):
        if level == 1:
            return random.randint(0, 9)
        if level not in [1, 2, 3]:
            raise ValueError()
        elif level == 2:
            return random.randint(10, 99)
        else:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()
