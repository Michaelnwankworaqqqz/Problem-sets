# Define main
def main():
    # Prompt user for meal's price and convert input to float using
    # dollar to float function
    dollars = dollars_to_float(input("How much was the meal? "))

    # Ask user for percentage of intended tip using percent to float function
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculate tip
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# Define functions
# Dollar to float and strip the $ in the p so it can be converted to a float
def dollars_to_float(d):
    d = d.replace('$', '')
    return float(d)

# Percent to float and make sure to replace the % sign with ''
def percent_to_float(p):
    p = p.replace('%', '')
    return float(p) / 100

main()
