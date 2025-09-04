def get_word_count(book_contents):
    split_book_contents = book_contents.split()

    return len(split_book_contents)

test_case = "The quick brown fox jumps over the big lazy dog's stupid house, Maddy!"
def get_character_counts(book_contents):
    character_counts = {}

    book_contents = book_contents.lower()
    for character in book_contents:
        if (character in character_counts) == False:
            character_counts[character] = 1
        else:
            character_counts[character] += 1

    return character_counts

def sort_on(items):
    return items["num"]

def sort_character_counts(character_counts):
    sorted_character_counts = []
    for count in character_counts:
        pair = {"char": count, "num": character_counts[count]}
        sorted_character_counts.append(pair)
    
    sorted_character_counts.sort(key=sort_on, reverse=True)

    return sorted_character_counts

#Function testing - Uncomment to test function if edits need to be made
#print(get_character_counts(test_case))
#print(sort_character_counts(get_character_counts(test_case)))