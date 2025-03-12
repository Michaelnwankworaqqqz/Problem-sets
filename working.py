import re
import sys


# Using try to print the called convert function on input, raising valueerror and exiting program via sys.exit()
def main():
        try:
            print(convert(input("Hours: ").upper()))
        except ValueError:
            sys.exit("ValueError")

# Defining the convert function
def convert(s):

    # Outlining the expected regex pattern of user's input
    time_pattern = (
        r"^(?P<first_hours>1[0-2]|[1-9])(?P<first_minutes>\:[0-5][0-9])?\s(?P<meridiem1>AM|PM)"
        r"\sto\s(?P<second_hours>1[0-2]|[1-9])(?P<second_minutes>\:[0-5][0-9])?\s(?P<meridiem2>AM|PM)$"
    )

    # Checking for matches and handling the lack of it via raise ValueError
    matches = re.search(time_pattern, s, re.IGNORECASE)
    if not matches:
        raise ValueError("ValueError")

    # Outlining groups in regex pattern
    if matches:
        start_hours = matches.group("first_hours")
        first_minutes = matches.group("first_minutes")
        meridiem1 = matches.group("meridiem1")
        end_hours = matches.group("second_hours")
        second_minutes = matches.group("second_minutes")
        meridiem2 = matches.group("meridiem2")


        # Converting hours to int
        start_hours = int(start_hours)
        end_hours = int(end_hours)


        # Conditioning input to properly match conversion of time from 12-hour to 24-hour format
        if meridiem1.upper() == "AM" and start_hours == 12:
             start_hours = 0

        if meridiem1.upper() == "PM"and not start_hours == 12:
            start_hours = start_hours + 12

        if meridiem2.upper() == "PM" and not end_hours == 12:
            end_hours = end_hours + 12

        elif meridiem2.upper() == "AM" and end_hours == 12:
            end_hours = 0


        if (meridiem1.upper() == "PM" and meridiem2.upper() == "PM") and (start_hours == 12 and end_hours == 12):
            start_hours = 12
            end_hours = 12

        if first_minutes == None:
            first_minutes = "00"
        else:
            first_minutes = int(first_minutes[1:])

        if second_minutes == None:
            second_minutes = "00"
        else:
            second_minutes = int(second_minutes[1:])

        if first_minutes == 60 or second_minutes == 60:
            raise ValueError("ValueError")

    # Reurning an formatted string of converted time
    return f"{start_hours:02}:{first_minutes:02} to {end_hours:02}:{second_minutes:02}"


if __name__ == "__main__":
    main()
