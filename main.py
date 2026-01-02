import sys
from stats import get_num_words, get_num_characters, sort_character_count

def get_book_text(file_path):
    with open(file_path) as f:
        book_content = f.read()
    return book_content

def main():
    if sys.argv.__len__() != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    sort_chartaters = sort_character_count(get_num_characters(book_text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for i in sort_chartaters:
        print(f"{i[0]}: {i[1]}")
    print("============= END ===============")
main()