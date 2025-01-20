# Define main
def main():
    # Prompt user for time
    time = input("What time is it? ")

    time = convert(time)

    print(meal_time(time))

# Define convert
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + minutes / 60

def meal_time(time):
    if time >= 7.00 and time <= 8.00:
       return("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        return("lunch time")
    elif time >= 18.00 and time <= 19.00:
        return("dinner time")
    

if __name__ == "__main__":
    main()
