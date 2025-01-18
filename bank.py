# Define main
def main():
    # Prompt user for a greeting
    greeting = input("Greeting: ").replace(" ", "").lower()

    # Call check_if
    check_if(greeting)

# Define check_if function
def check_if(string):
    # Return $0 if greeting starts with "Hello"
    if string.lower().startswith("hello"):
        print("$0")
    # Return $20 if greeting starts with "H"
    elif string.lower().startswith("h"):
        print("$20")
    # Return $100 for any other greetings
    else:
        print("$100")


main()
