import time
import requests

url = "https://discord.com/api/v8/users/@me/settings"

# Use raw string for file path
File = open(r"C:\Users\gopal\Downloads\brutalbeerus.txt", "r")
lines = File.readlines()

def ChangeStatus(message):
    header = {
        "authorization": "MTA1NDM4MDc3NTI3NDk3NTI0Mg.G_wywB.djq4GglOh4Y6GwhDRiX7Pf0YSPAxGO7ix-m8q4"
    }

    jsonData = {
        "status": "dnd",
        "custom_status": {
            "text": message
        }
    }

    try:
        response = requests.patch(url, headers=header, json=jsonData)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx and 5xx)
        print(f"Status changed to: {message}")
    except requests.RequestException as e:
        print(f"Error changing status: {e}")

while True:
    for line in lines:
        ChangeStatus(line.strip())  # Use strip to remove leading/trailing whitespaces
        time.sleep(2)
