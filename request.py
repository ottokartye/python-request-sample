import requests
import json
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://jsonplaceholder.typicode.com/users")
print(f"\nStatus code: {bcolors.WARNING}{response.status_code}{bcolors.ENDC}")
for idx, user in enumerate(response.json()):
    index = f" {idx}" if (idx) < 10 else f"{idx}"
    print(f"{index}: Name: {user['name']} | Username: {bcolors.WARNING}{user['username']}{bcolors.ENDC} | Email: {bcolors.BOLD}{user['email']}{bcolors.ENDC}")

# Shows the home directory of the current user.
print(f"Your current woring directory is: ")
os.system("pwd")
