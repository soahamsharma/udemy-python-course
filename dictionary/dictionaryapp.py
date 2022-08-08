import json
from difflib import get_close_matches

# load the dictionary file
source = json.load(open('data.json', 'r'))

def main():
    # Get word from user
    word = input("Please enter the word you want the definition for: ")
    word = word.lower()

    # print definition(s)
    if word in source:
        result = source[word]
    elif len(get_close_matches(word, source.keys(), cutoff=0.8)) != 0:
        possible = get_close_matches(word, source.keys())[0]
        response = input("Did you mean "+possible+"?")
        if response.startswith("y"):
            result = source[possible]
        else:
            result = ["No result"]
    else:
        result = ["No such word"]

    for answer in result:
        print (answer)

main()