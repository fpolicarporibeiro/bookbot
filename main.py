def main():
    book_path = "/Users/franciscoribeiro/workspace/github.com/fpolicarporibeiro/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters  = get_num_characters(text)
    num_unique_characters = get_num_characters(text)
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n")
    print_report(num_words, num_characters)
    print(f"--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lowered_text = text.lower()
    unique_character_count = {}
    for character in lowered_text:
        if character in unique_character_count:
            unique_character_count[character] += 1
        else:
            unique_character_count[character] = 1
    return unique_character_count

def sort_on(dict):
    return dict["num"]

def print_report(num_words, unique_character_count):
    unique_character_list = []
    for character, count in unique_character_count.items():
        if character.isalpha():
            unique_character_dict = {"character": character, "num": count}
            unique_character_list.append(unique_character_dict)

    unique_character_list.sort(reverse=True, key=sort_on)

    for char_dict in unique_character_list:
        print(f"The '{char_dict['character']}' character was found {char_dict['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
