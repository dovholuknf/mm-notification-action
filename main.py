import sys
import os
import requests

def main(param1, param2):
    print(f"Input1 was: {param1}")
    print(f"Input2 was: {param2}")
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API call succeeded.")
    else:
        print("GitHub API call failed.")

    return "Process completed."

if __name__ == "__main__":
    param1 = os.getenv("example_input")
    param2 = os.getenv("example_input2")
    result = main(param1, param2)
    print(f"Output: {result}")
