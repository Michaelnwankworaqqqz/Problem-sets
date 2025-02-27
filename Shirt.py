# Importing appropriate modules
from PIL import Image

from PIL import ImageOps

import os

import sys

def main():
    # Opening the shirt and defining size
    shirt = Image.open("shirt.png")
    size = shirt.size

    # Checking command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Checking that coomand line is either .jpg, .jpeg, or .png file
    elif not sys.argv[1].lower().endswith((".jpg", ".jpeg", ".png")) and not sys.argv[2].lower().endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")

    # Checking that files exists
    elif not os.path.exists(sys.argv[1]) and not os.path.exists(sys.argv[2]):
        sys.exit("Input does not exit")

    # Checking that both inputs has the same extensions
    elif not sys.argv[1][sys.argv[1].rfind("."):] == sys.argv[2][sys.argv[2].rfind("."):]:
        sys.exit("Input and output have different extensions")

    # Opening image as command-line argument(Input)
    image = Image.open(sys.argv[1])

    # Resizing and croping image
    image = ImageOps.fit(image, size)

    # Overlaying shirt
    image.paste(shirt, shirt)

    # Saving image as output(Second command-line argument)
    image.save(sys.argv[2])


main()
