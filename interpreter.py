# Define main
def main():

    # Prompt user for an arithemetic expression
    expression = (input("Enter arithmetic: "))
    x, y, z = expression.split(" ")

    # Convert x, and z to a floating point value
    x = float(x)
    z = float(z)

    # Call calculate
    answer = calculate(x, y, z)

    # Round expression(answer) to one(1) decimal place
    answer = round(answer, 1)

    print(answer)

# Define calculate
def calculate(a, b, c):
    if b == "+":
        return a + c
    elif b == "-":
        return a - c
    elif b == "*":
        return a * c
    else:
        return a / c

main()
