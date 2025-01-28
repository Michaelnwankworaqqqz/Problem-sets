def main():
    while True:
        try:
            # Prompt user for fraction in the formatof x / y
            fraction = (input("Fraction: "))

                     # Split user's input into x and y
            x, y = fraction.split("/")

            # Convert x and y to integers
            x = int(x)
            y = int(y)

            # Calculate the percentage of x and y
            percent = x / y * 100
            result = round(percent)

            # Print result
            print(percentage(result))

            # Exit loop if all goes well
            break

        # Catch any Exceptions
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

# Print percentage result
def percentage(r):
    if r <= 1:
        return "E"
    elif r >= 99:
        return "F"
    else:
        return f"{r}%"

main()
