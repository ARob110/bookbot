from stats import get_word_count
from stats import get_char_count
from stats import sort_dict
from stats import sort_num
import sys

print("Usage: python3 main.py <path_to_book>")

if len(sys.argv) != 2:
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        return book_text
    
def main():
    book = get_book_text(sys.argv[1])
    count = get_word_count(book)
    charCount = get_char_count(book)
    charSort = sort_dict(charCount)
    print(f"Found {count} total words")

    for item_dict in charSort:
        if item_dict["char"].isalpha():
            print(f"{item_dict["char"]}: {item_dict["num"]}")

main()