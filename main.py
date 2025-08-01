import sys
from stats import count_num_words, frequency_of_character, sort_characters

def get_book_text(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    return content


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_num_words(book_text)
    print(f"{num_words} words found in the document")
    
    char_counts = frequency_of_character(book_text)
    sorted_characters = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character_num in sorted_characters:
        if character_num["char"].isalpha():
            print(f"{character_num["char"]}: {character_num["num"]}")
    print("============= END ===============")

main()