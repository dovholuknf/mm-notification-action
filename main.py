import sys
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
    param1 = sys.argv[1] if len(sys.argv) > 1 else "No Input Provided"
    param2= sys.argv[2] if len(sys.argv) > 2 else "No Input Provided"
    result = main(param1, param2)
    print(f"Output: {result}")
