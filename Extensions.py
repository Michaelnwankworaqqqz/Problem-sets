# Define main
def main():
    # Prompt user for name of file
    file_name = input("File name: ").lower().strip()

    # Call file_tpe
    file_type(file_name)

# Define file_type
def file_type(string):
    if string.lower().endswith(".gif"):
        print("image/gif")
    elif string.lower().endswith(".jpg") or string.lower().endswith(".jpeg"):
        print("image/jpeg")
    elif string.lower().endswith(".png"):
        print("image/png")
    elif string.lower().endswith(".pdf"):
        print("application/pdf")
    elif string.lower().endswith(".txt"):
        print("text/plain")
    elif string.lower().endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
