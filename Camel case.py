def main():
    # Prompt user for input in camel case
    CamelCase = input("Enter string in camel case: ")

    # Print out in snake case
    snake_case = convert_case(CamelCase)
    print(snake_case)

def convert_case(string):
    # Initialize an empty list
    answer = []
    # Loop through camel case string
    for s in string:
        # add an underscore after any uppercased character
        if s.isupper():
            answer.append("_")
            # Lowercase all characters in the list
            s = s.lower()
            # Append string to list
            answer.append(s)
        # If no uppercase is found
        else:
            answer.append(s)
    # Join list to a string that supports snake_case
    snake_case_string = ("".join(answer))
    return snake_case_string

main()
