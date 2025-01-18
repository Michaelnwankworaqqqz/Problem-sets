# Define main
def main():
    # Prompt user for the answer to the question
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? "
                   ).replace(" ", "").replace("-", "").lower()
    answer = "Forty two".replace(" ", "").replace("-", "").lower()

    # user input must be case insesitive
    check(question, answer)

# Define a function that prints out yes only when the user input == 42(case insensitive)
def check(string, answer):
    if answer == string or string == "42":
        print("Yes")
    else:
        print("No")

# Call main
main()
