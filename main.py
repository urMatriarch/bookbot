from stats import get_word_count, get_character_counts, sort_character_counts, sort_on
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    book_contents = ""
    
    with open(filepath) as f:
        book_contents = f.read()
    
    return book_contents

def main():
    path_to_file = sys.argv[1]
    book_contents = get_book_text(path_to_file)

    word_count = get_word_count(book_contents)
    #print(f"{word_count} words found in the document")

    character_counts = get_character_counts(book_contents)
    #print(character_counts)

    sorted_character_counts = sort_character_counts(character_counts)

    #time to print!!!!
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in sorted_character_counts:
        print(f"{pair["char"]}: {pair["num"]}")

main()