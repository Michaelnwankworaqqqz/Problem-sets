import os
import sys

def main():
    # Expect one command-line arg, should end with .py, and must exist.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argumets")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")

    # Assigning sys.argv[1] to a variable
    new_file = sys.argv[1]

    # Creating counter variables to ensure adequate counting of LOC, Comments, and Blank lines
    blank_counter = 0
    comment_counter = 0
    line_counter = 0

    # Opening and reading file per each line
    with open(new_file) as file:
        for line in file:
            line = line.strip()

            # Updating blank_counter
            if line == "":
                blank_counter += 1

            # Updating comment_counter
            elif line.startswith("#"):
                comment_counter += 1

            # Updating line_counter
            else:
                line_counter += 1

    # Print number of lines
    print(f"Number of lines = {line_counter}")


main()
