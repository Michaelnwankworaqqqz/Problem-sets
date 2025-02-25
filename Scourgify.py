import csv

import os

import sys

def main():

    names = []

    # Expect two command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check that sys.argv[1] is a CSV file
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Could not read 1.csv")

    # Check if file exist
    elif not os.path.exists(sys.argv[1]):
        sys.exit(f"Could not read {sys.argv[1]}")


    # Open file for reading and writing
    with open(sys.argv[1]) as before, open(sys.argv[2], "w") as after:

        # Read file
        reader = csv.DictReader(before)

        # Write to file
        writer = csv.DictWriter(after, fieldnames=["name", "house"])

        # Write headers to new csv file
        writer.writeheader()

        # Split the name so you can update the name format
        for row in reader:
            last_name, first_name = row["name"].split(", ")
            full_name = f"{first_name}, {last_name}"
            house = row["house"]

            # Write data into new csv file
            writer.writerow({"name": full_name, "house": house})


main()
