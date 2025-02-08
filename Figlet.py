# Import modules and libraries needed for to run program
from pyfiglet import Figlet
import random
import sys

# Create a list of fonts to compare arguments with
figlet_instance = Figlet()
fonts = figlet_instance.getFonts()

def main():
    valid_args = None

    #Expects zero or two command-line arguments:
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("inadequate arguments")

    # Two if the user would like to output text in a specific font,
    if len(sys.argv) == 3:

        # in which case the first of the two should be -f or --font,
        # and the second of the two should be the name of the font.
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
            valid_args = True
        else:
            sys.exit("Unacceptabe command-line arguments")

    # Prompts the user for a str of text.
    text = input("Input: ")

    # Set fonts according to user's choice of input method
    if valid_args == True:
        # Set font
        figlet_instance.setFont(font=sys.argv[2])

        #Outputs that text in the desired font.
        print(figlet_instance.renderText(text))
    else:
        # Set font to random
        figlet_instance.setFont(font=random.choice(fonts))

        #Outputs that text in random font
        print(figlet_instance.renderText(text))

main()
