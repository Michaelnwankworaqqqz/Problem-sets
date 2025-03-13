import re
import sys

def main():
    # Print out the output of calling count on input
    print(count(input("Text: ")))


# Define the count function
def count(s):
    # Initialize a counts variable for keeping tracks of matches found
    counts = 0

    # Implement the regex pattern of expected word
    word_pattern = r"\bum\b"

    # Call re.findall to get matches
    matches = re.findall(word_pattern, s, re.IGNORECASE)

    # Iterate through matches and increment counts for every match found/made
    for _ in matches:
        counts+= 1

    # Return counts
    return counts

if __name__ == "__main__":
    main()
