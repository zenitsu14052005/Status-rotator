import sys, os, time, requests, random
# from dotenv import load_dotenv, find_dotenv
# load_dotenv(find_dotenv())
# Token = "Add your token"
from token import *
class Discord:

    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": MTA1NDM4MDc3NTI3NDk3NTI0Mg.G_wywB.djq4GglOh4Y6GwhDRiX7Pf0YSPAxGO7ix-m8q4,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*"
        }

    def ChangeStatus(self, status, message, emoji_name, emoji_id):
        jsonData = {
            "status": status,
            "custom_status": {
                "text": message,
                "emoji_name": emoji_name,
                "emoji_id": emoji_id,
        }}
        r = requests.patch("https://discord.com/api/v8/users/@me/settings", headers=self.headers, json=jsonData)
        print(r.text)
        return r.status_code

import time

def Run(discord, status):
    file_path = 'status.txt'

    while True:
        # Open the file and read all lines into a list
        with open(file_path, 'r') as file:
            messages = [line.strip() for line in file.readlines()]

        # Check if there is at least one message
        if not messages:
            print("No messages found in the file. Add messages to continue.")
            time.sleep(10)  # Wait for 10 seconds before trying again
            continue

        # Iterate over each message
        for message in messages:
            # Split the message using a comma as a separator
            message_parts = message.split(',')

            # Check if there are enough parts in the message
            if len(message_parts) >= 2:
                # Extract emoji information
                emoji_id = None
                emoji_name = message_parts[0].strip()

                # Check if the emoji_name starts with a number
                if emoji_name and emoji_name[0].isdigit():
                    emoji_id = emoji_name
                    emoji_name = ""

                # Extract status from the second part
                status_text = message_parts[1].strip()

                # Update the status
                status_code = discord.ChangeStatus(status, status_text, emoji_name, emoji_id)

                # Print feedback
                if status_code == 200:
                    print("|———————————————————————————————————|")
                    print("  Changed your status! ")
                    print(f"  Emoji ID: {emoji_id}")
                    print(f"  Emoji Name: {emoji_name}")
                    print(f"  Status: {status_text}")
                    print("|———————————————————————————————————|")
                else:
                    print("An error occurred. Try again?")

            # Wait for 10 seconds before updating with the next message
            time.sleep(10)





def Main():
    discord = Discord(TOKEN)
    while True:
        Run(discord, "dnd") # Change circle status | dnd, idle, online
        time.sleep(3)

Main()


