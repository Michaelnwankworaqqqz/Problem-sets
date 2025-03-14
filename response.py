# Import libraries
import validators


def main():
    # Prompt user for email address
    email = input("What's your email address? ")


    # Check user's input(email) using validator
    if validators.email(email):
        # Print valid if user's input passes check, else print invalid
        print("Valid")
    else:
        print("invalid")


main()
