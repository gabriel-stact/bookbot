

def count_num_words(text):
    words = text.split()
    return len(words)

def frequency_of_character(text):
    text = text.lower()
    frequency = {}
    for char in text:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    
    return frequency

def sort_on(items):
    return items["num"]

def convert_dictionary(items):
    characters = []
    new_dict = {}
    for item, value in items.items():
        new_dict["char"] = item
        new_dict["num"] = value
        characters.append(new_dict.copy())
    return characters

def sort_characters(characters_dict):
    characters = convert_dictionary(characters_dict)
    characters.sort(reverse=True, key=sort_on)
    return characters