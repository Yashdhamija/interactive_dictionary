import json
from difflib import get_close_matches

dict = json.load(open("data.json"))

def meaning(key):
        try:
            #the keys exist in the data as either:
            # title e.g. Delhi
            if key.capitalize() in dict:
                return dict[key.capitalize()]
            # Acronyms e.g. USA
            elif key.upper() in dict:
                return dict[key.upper()]
            # lower cased string
            else:
                return dict[key]

        except KeyError:
            suggestion = get_close_matches(key, dict.keys(), 1)
            if len(suggestion):
                answer = input(f"Did you mean {suggestion[0]} instead? (Type y/yes or n/no): ").lower()
                if answer in ('y', 'yes'):
                    return dict[suggestion[0]]
                elif answer in ('n', 'no'):
                    return "Sorry, the word could not be interpreted"
                else:
                    return "Sorry, I couldn't understand your query"
            else:
                return "Sorry, the word could not be interpreted"

word = input("Enter word: ")

output = meaning(word.lower())
if type(output) == list:
    if len(output) > 1:
        for definitions, i in zip(output,range(len(output))):
            print(f"{i+1}. " + definitions)
    else:
        print(output[0])
else:
        print(output)
