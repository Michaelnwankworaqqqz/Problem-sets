import re
import sys


def main():
    # Printing the output of calling the parse function on user's input
    print(parse(input("HTML: ")))


# Defining the parse function
def parse(s):
    # Outlining html regular expression pattern
    html_pattern = (
        r"^\<iframe\s(?:width\=\"560\"\sheight\=\"315\"\s)?"
        r"(?:src\=)(?P<src>\"https?://(?:www\.)?youtube\.com/embed/[a-zA-z0-9]+\")"
        r"(?:\stitle\=\"YouTube\svideo\splayer\"\sframeborder\=\"\d\"\sallow\=\"accelerometer\;"
        r"\sautoplay\;\sclipboard\-write\;\sencrypted\-media\;\sgyroscope\;\spicture\-in\-picture\"\sallowfullscreen)?\>\<\/iframe\>$"
    )
    #Checking for matching between html pattern and user input
    matches = re.search(html_pattern, s, re.IGNORECASE)
    if matches:
         # Conditioning user input
        if "https" in matches.group("src"):
            src_code = matches.group("src").lstrip('"').replace("www.", "").replace("youtube", "youtu.be/")\
                .replace(".com/embed/", "").rstrip('"')
        elif "http" in matches.group("src"):
            src_code = matches.group("src").lstrip('"').replace("http", "https").replace("www.", "")\
                .replace("youtube", "youtu.be/")\
                .replace(".com/embed/", "").rstrip('"')
        return src_code
    else:
        return None


if __name__ == "__main__":
    main()
