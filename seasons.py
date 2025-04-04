from datetime import datetime, date
import inflect
import re
import sys


p = inflect.engine()


def main():
    # Prompt user for date of birth in YYYY-MM-DD format
        try:
            date_of_birth = input("DOB: ")
            dob = datetime.strptime(date_of_birth, "%Y-%m-%d")
        except:
             sys.exit("Invalid date")


        # Calling the DOB in minutes calculator function of dob
        dob_in_minutes = age_in_minutes_calc(dob)

        # Converting rounded age in minutes to words via the inflect module function
        worded_dob = p.number_to_words(dob_in_minutes)


        # Print out how old they are in minutes rounded in the nearest integer in words rathan numerals
        new_worded_dob = re.sub(r"\s*\band\b\s*", " ", worded_dob)
        print(f"{new_worded_dob[0].upper() + new_worded_dob[1:]} minutes")


# calculate the user's age in minute
def age_in_minutes_calc(date_of_birth):
    timedelta = date.today() - date_of_birth.date()
    number_seconds = timedelta.total_seconds()
    # Rounding the result of user's age in minutes to the nearest integer
    return round(number_seconds / 60)


if __name__ == "__main__":
    main()
