# Declare a const variable for speed of light
light_speed = 300000000

# Def main
def main():
    # Prompt user for input and convert said input to an int in kilograms
    kilograms = int(input("Enter kilograms: "))

    # Convert int(kilograms) to equivalent in joules
    joules = kilograms * pow(light_speed, 2)

    # Print int(joules)
    print(f"{joules}")

# Call main
main()
