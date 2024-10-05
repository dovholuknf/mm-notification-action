import argparse
import requests


def main(args):
    print(f"Input1 was: {args.identityFile}")
    print(f"Input2 was: {args.githubEvent}")
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("GitHub API call succeeded.")
    else:
        print("GitHub API call failed.")

    return "Process completed."


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--identityFile', type=str, default="No Input Provided")
    parser.add_argument('--githubEvent', type=str, default="No Input Provided")

    args = parser.parse_args()

    result = main(args)
    print(f"Output: {result}")
