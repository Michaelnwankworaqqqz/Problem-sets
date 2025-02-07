# Import module
import emoji

# Create a dictionary to handle variations
variations = {
    ":thumbsup:": ":thumbs_up:",
    ":smilecat:": ":smile_cat:",
}

def main():
    # Prompt user for string in english
    string = input("Input: ")

    # Output the emojized version of user's input
    for variant in variations:
        string = string.replace(variant, variations[variant])
    print(f"Output: {emoji.emojize(string)}")

main()
