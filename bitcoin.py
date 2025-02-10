# Import modules/Libraries
import requests
import sys

def main():
    # Command line argument (number of bitcoins) and checks
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Converting command-line to arguments
    num_bitcoins = float(sys.argv[1])

    # Request API for the coin desk bitcoin price
    try:
        response = requests.get(
        " https://api.coindesk.com/v1/bpi/currentprice.json"
        )

    except requests.RequestException:
        print("Unable to process API request")

    data_file = response.json()

    # Convert Quantity of bitcoin inputted as command-line to bitcoin
    amount = num_bitcoins * 37817.3283

    # Print price equivalent of qty of bitcoin
    print(f"${amount:,.4f}")


main()
