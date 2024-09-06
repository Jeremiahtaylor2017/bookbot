def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    char_list = dict_to_list(char_count)
    char_list.sort(reverse=True, key=sort_on)
    generate_report(book_path, word_count, char_list)


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_on(char_dict):
    return list(char_dict.values())[0]


def dict_to_list(char_dict):
    my_list = []
    for char in char_dict:
        if char.isalpha():
            my_list.append({char: char_dict[char]})

    return my_list


def generate_report(book_path, word_count, char_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char_dict in char_list:
        for char in char_dict:
            print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
