import requests
import json
import random
import sys


def get_random_words(amount):
    url = "https://random-word-api.herokuapp.com/word?number={}".format(amount)
    response = requests.get(url)
    words = json.loads(response.text)
    return words # thansk you copilot for the code

def run_program_with_args():
    args = sys.argv()
    first_args = ["--help", "--password", "--wizard"]
    if args[1] in first_args:
        if args[1] == "--help":
            print("--wizard: Generates a password with a wizard")
            print("--password: Generates a password")
            print("--help: Shows the available commands")
        elif args[1] == "--password":
            if (not args[2].isnumeric() ):
                print("Invalid number")
                return
            
        elif args[1] == "--wizard":
            print("Generating a password with a wizard")
            
    else:
        print("Invalid command")
        print("Use --help to see the available commands")
