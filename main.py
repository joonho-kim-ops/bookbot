import sys
from stats import word_count
from stats import char_count
from stats import sort_char

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    # Report sorted character counts

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")

    list = sort_char(char_count(book_text))
    for char, count in list.items():
        print(f"{char}: {count}")

    print("============= END ===============")
def get_book_text(file):
    with open (file) as f:
        file_contents = f.read()
    return file_contents



main()