import re
import sys


def main():
    # Call validate on input and print
    print(validate(input("IPv4 Address: ")))


# Define validate function
def validate(ip):
    pattern = (
        r"^([0-9]|[1-9][\d]|1[\d][\d]|2[0-4][\d]|25[0-5])\."
        r"([0-9]|[1-9][\d]|1[\d][\d]|2[0-4][\d]|25[0-5])\."
        r"([0-9]|[1-9][\d]|1[\d][\d]|2[0-4][\d]|25[0-5])\."
        r"([0-9]|[1-9][\d]|1[\d][\d]|2[0-4][\d]|25[0-5])$"
    )

    match = re.search(pattern, ip)
    if match:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
