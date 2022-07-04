import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def explane(w):
    if w.lower() in data:
        return data[w.lower()]
    elif len(get_close_matches(w.lower(),data.keys())) > 0:
        print("Did u mean <%s> instead?" %get_close_matches(w.lower(),data.keys())[0])
        if (input("Enter <Y> if yes\nEnter <T> if no\n")) == "Y":
            return data[get_close_matches(w.lower(),data.keys())[0]]
        return "The word doesnt't exist. Please try again."
    else:
        return "The word doesnt't exist. Please try again."

word = input("Enter a word: ")

output = explane(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
