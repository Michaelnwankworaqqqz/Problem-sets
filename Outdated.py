calender = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    month_num = None
    # Prompt user for date in month-day-year order
    while True:
            date = input("Date: ")
            if '/' in date:
                 date = date.split('/')
            elif ',' in date:
                 date = date.split(',')
                 date = date[0].split() + [date[1].strip()]
            else:
                 date = date.split()

            if len(date) != 3:
                 break
            date01 = date[0]
            date02 = date[1]
            date03 = date[2]

            # Check input validity

            # Ensure that no month has above 31 days
            if date01 in calender:
               month_num = calender[date01]
            elif date01.isdigit() and 1 <= int(date01) <= 12:
                 date01 = int(date01)
            else:
                 continue

            date02 = date02.strip(',')
            if not date02.isdigit() or not (1 <= int(date02) <= 31):
                 continue

            if len(date03) != 4 or not date03.isdigit():
                 continue
            else:
                 if month_num is not None:
                    # Output that same date in YYYY-MM-DD format
                    print(f"{date03}-{month_num:02}-{int(date02):02}")
                    break
                 else:
                    print(f"{date03}-{int(date01):02}-{int(date02):02}")
                    break

main()
