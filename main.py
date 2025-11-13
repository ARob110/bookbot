from stats import get_word_count
from stats import get_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        return book_text
    
def main():
    book = get_book_text("books/frankenstein.txt")
    count = get_word_count(book)
    charCount = get_char_count(book)
    print(f"Found {count} total words")
    print(charCount)

main()