def main():
    grocery_list = {}
    # Prompt user for items one per line(.lower()) until input == ctrl-d
    while True:
        try:
            item = input().lower()
        except EOFError:
            break
        # Add each itea=m to dictionary and update count if item is already in dictionary
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    # Output user's list all in uppercase sorted alphabetical order
    new_dict = sorted(grocery_list.keys())
    for grocery in new_dict:
        print(f"{grocery_list[grocery]} {grocery.upper()}")

main()
