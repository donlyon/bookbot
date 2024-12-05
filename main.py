def main():
    book_path = "books/frankenstein.txt"

    print(f"--- Begin report of {book_path} ---")
    text = get_text(book_path)

    count = count_words(text)
    print(f"{count} words found in the document.\n")

    letters = sort_letters(text)
    for items in letters:
        print(f"The '{items['letter']}' character was found {items['count']} times")

    print("--- End report ---")

def get_text(book_path):
    with open(book_path) as file:
        text = file.read()

    return text

def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["count"]

def sort_letters(text):
    result = []
    chars_dict = {}
    lowered = text.lower()
    for letter in lowered:
        if letter.isalpha():
            if letter in chars_dict:
                chars_dict[letter] += 1
            else:
                chars_dict[letter] = 1

    for ch in chars_dict:
        result.append({"letter": ch, "count": chars_dict[ch]})
    result.sort(reverse=True, key=sort_on)
    return result

main()
