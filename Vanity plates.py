def main():
    # Prompt user for input of plate number
    plate = input("Plate: ")

    # Check if plate's valid
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# All vanity plates must start with at least two letters
def plate_start(plate):
    if plate[0:2].isalpha():
        return "valid"
    else:
        return "invalid"


# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def plate_content(plate):
    if len(plate) < 2 or len(plate) > 6:
        return "invalid"
    else:
        return "valid"

# Numbers cannot be used in the middle of a plate; they must come at the end
def complate(plate):
    for p in range(1, len(plate) - 1):
        if plate[p].isdigit() and plate[p - 1].isalpha():
            return "invalid"
        return "valid"

# The first number used cannot be a ‘0’.
def acceptable(plate):
    for p in plate:
        if p.isdigit():
            if p == '0':
                return "invalid"
            break
    return "valid"

# No periods, spaces, or punctuation marks are allowed
def no_punct(plate):
    table = plate.maketrans("", "", ".,:;'!/?)(}{][ ")
    new_string = plate.translate(table)
    return new_string


# Function that checks if plate's valid or not
def is_valid(s):
    if plate_start(s) == "invalid":
        return False
    if plate_content(s) == "invalid":
        return False
    if complate(s) == "invalid":
        return False
    if acceptable(s) == "invalid":
        return False
    if no_punct(s) != s:
        return False
    return True


main()
