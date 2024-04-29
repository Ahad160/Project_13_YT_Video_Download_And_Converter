import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Download a file from a URL")

# Define the command-line arguments
parser.add_argument("-d", action="store_true", help="Download the file")
parser.add_argument("-u", type=str, help="URL to download from")
parser.add_argument("-cp", type=str, help="Path to save the downloaded file")

# Parse the command-line arguments
args = parser.parse_args()

# Check which options were provided by the user
if args.d:
    print("Downloading file...")
    if args.u:
        url = args.u
        print(f"URL: {url}")
    else:
        print("Error: -u option requires a URL.")
    if args.cp:
        path = args.cp
        print(f"Save path: {path}")
    else:
        print("Error: -cp option requires a path.")
else:
    print("Error: -d option is required to initiate the download.")
