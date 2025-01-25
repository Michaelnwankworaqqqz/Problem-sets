def main():
    # Prompt user for str text
    text = input("Input: ")

    # Shorten text
    shortened_text = remove_vowel(text)

    # Output user's input without vowels(whether inputted in lowercase or uppercase)
    print(f"Output: {shortened_text}")

def remove_vowel(phrases):
    # Empty str variable
    new_phrase = ""

    # For loop to iterate through phrases
    for phrase in phrases:

        # Handle vowels with replace str method(uppercase and lowercase)
        phrase = phrase.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
        phrase = phrase.replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", "")

        # Concatenate phrases into empty str variable and return
        new_phrase += phrase

    return new_phrase

main()
