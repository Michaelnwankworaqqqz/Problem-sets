# DEfine main
def main():
    # Prompt user for string
    emostring = input("PLease enter a string with emojis: ")

    # Call convert function
    print(convert(emostring))


# Define a function called convert
def convert(string):
    s = (string.replace(':(', '🙁').replace(':)', '🙂'))
    return s

# Call main
main()
