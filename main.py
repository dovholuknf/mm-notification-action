import sys
import requests

def main(param1):
    print(f"Input was: {param1}")
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API call succeeded.")
    else:
        print("GitHub API call failed.")

    return "Process completed."

if __name__ == "__main__":
    param1 = sys.argv[1] if len(sys.argv) > 1 else "No Input Provided"
    result = main(param1)
    print(f"Output: {result}")
