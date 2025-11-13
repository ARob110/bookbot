from stats import get_word_count
from stats import get_char_count
from stats import sort_dict
from stats import sort_num

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        return book_text
    
def main():
    book = get_book_text("books/frankenstein.txt")
    count = get_word_count(book)
    charCount = get_char_count(book)
    charSort = sort_dict(charCount)
    print(f"Found {count} total words")

    for item_dict in charSort:
        if item_dict["char"].isalpha():
            print(f"{item_dict["char"]}: {item_dict["num"]}")

main()