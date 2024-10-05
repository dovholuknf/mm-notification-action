import sys
import requests

def main(input_value):
    print(f"Input was: {input_value}")
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API call succeeded.")
    else:
        print("GitHub API call failed.")

    return "Process completed."

if __name__ == "__main__":
    input_value = sys.argv[1] if len(sys.argv) > 1 else "No Input Provided"
    result = main(input_value)
    print(f"Output: {result}")
