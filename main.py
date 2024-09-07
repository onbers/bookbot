def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(book):
    words = book.split()
    return len(words)

def get_character_count(text):
    lowered_string = text.lower()
    character_count = {}

    for c in lowered_string:
        if c not in character_count:
            character_count[c] = 1
        else:
            character_count[c] += 1

    return character_count

def dicts_to_list(char_dict):
    list_of_dicts = []
    for key in char_dict:
        if key.isalpha():
            temp_dict = {"char": key, "count": char_dict[key]}
            list_of_dicts.append(temp_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

def display_report(word_count, sorted_char_count, book_path):
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for d in sorted_char_count:
        temp_char = d["char"]
        temp_count = d["count"]
        print(f"The '{temp_char}' character was found {temp_count} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["count"]
    

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = get_word_count(text)

    character_count = get_character_count(text)

    sorted_character_count = dicts_to_list(character_count)

    display_report(word_count,sorted_character_count, book_path)


main()