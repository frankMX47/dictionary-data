import json
import difflib

def load_dictionary(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)

def get_definition(word, dictionary):
    word = word.lower()  # Convert word to lowercase for case-insensitive search
    if word in dictionary:
        return dictionary[word]
    else:
        # Find the closest word in the dictionary using difflib
        closest_matches = difflib.get_close_matches(word, dictionary.keys(), n=1)
        if closest_matches:
            closest_word = closest_matches[0]
            suggestion = f"Did you mean '{closest_word}'?"
            return suggestion
        else:
            return "Word not found in the dictionary."

def main():
    dictionary = load_dictionary('dictionary.json')

    while True:
        word = input("Enter a word to search for its definition (or 'exit' to quit): ")
        if word.lower() == 'exit':
            break
        definition = get_definition(word, dictionary)
        print(definition)

if __name__ == "__main__":
    main()
