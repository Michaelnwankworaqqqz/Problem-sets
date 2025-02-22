# Handle imports
from tabulate import tabulate

import csv

import os

import sys

def main():
    # A list to store tabulated Data
    read_file = []

    # Command-line arguments checks

    # Check for less than one argument
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # Check for more than one arguments
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # Check that argument is a csv file
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    # Check that file exists
    elif not os.path.exists(sys.argv[1]):
        sys.exit("File does not exist")

    # OPen, read, and tabulate file
    with open(sys.argv[1]) as file:
        reader = csv.reader(file, )
        headers = next(reader)
        read_file = tabulate(reader, headers, tablefmt="grid")

    # Output tabulted file
    print(f"{read_file}")

main()
