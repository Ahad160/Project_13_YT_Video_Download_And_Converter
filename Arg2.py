import argparse

# Custom action to convert the argument to lowercase
def lowercase_action(arg):
    s=arg.lower
    return s

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Download a file from a URL")

# Define the command-line arguments
parser.add_argument("-d", action="store_true", help="Download the file")
parser.add_argument("-u", type=str, help="URL to download from")
parser.add_argument("-cp", type=lowercase_action(str), help="Path to save the downloaded file")

# Prompt the user for the command line input
user_input = input("Enter the command line: ")

# Split the user input into a list of arguments
user_args = user_input.split()

# Parse the user-supplied command-line arguments
args = parser.parse_args(user_args)

# Check if the -d flag is provided to initiate the download
if args.d:
    if args.u:
        url = args.u
    else:
        url = input("Enter the URL to download from: ")

    if args.cp:
        path = args.cp
    else:
        path = input("Enter the path to save the downloaded file: ")

    print(f"Downloading file from URL: {url}")
    print(f"Saving file to path: {path}")
else:
    print("Error: -d option is required to initiate the download.")
