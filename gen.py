import requests
import json
import random
import sys


def get_random_words(amount):
    url = "https://random-word-api.herokuapp.com/word?number={}".format(amount)
    response = requests.get(url)
    words = json.loads(response.text)
    return words # thansk you copilot for the code


def passwordGenerator(amt_words, numb_size):
    words = get_random_words(amount=amt_words)
    password = ""
    for word in words:
        password += word.capitalize()
    password += str(random.randint(0, numb_size))
    return password


def passwordGeneratorV2(amt_tings):

    formatter_keywords = ["num", "str"]
    formatter = []
    words = get_random_words(amount=amt_tings) # yeah yeah its wastes bandwidth but i dont care
    result = ""

    for i in range(amt_tings):
        formatter.append(random.choice(formatter_keywords))
    counter = 0
    for type in formatter:
        counter += 1
        if type == "num":
            result += str(random.randint(0, 9))
        elif type == "str":
            result += words[counter - 1].capitalize()

    return result
    


def run_program_with_args():
    args = sys.argv
    first_args = ["--help", "--password", "--wizard"]

    if len(args) < 2:
        print("Please specify a command\nUse --help to see the commands")
        return

    if args[1] in first_args:
        if args[1] == "--help":
            print("--wizard: Generates a password with a wizard")
            print("--password: Generates a password")
            print("--help: Shows the available commands")
        elif args[1] == "--password":
            try:
                if (args[2].isnumeric()):
                    args[2] = int(args[2])
                    #print(passwordGenerator(amt_words=args[2], numb_size=args[2] * 10))
                    print(passwordGeneratorV2(amt_tings=args[2]))
                    return
            except IndexError:
                print("ERROR: Usage --password <amount>")
                return

            
        elif args[1] == "--wizard":
            print("Generating a password with a wizard")
            
    else:
        print("Invalid command")
        print("Use --help to see the available commands")

run_program_with_args()