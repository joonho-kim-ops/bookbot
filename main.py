def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(f"Found {word_count(book_text)} total words")

def get_book_text(file):
    with open (file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

main()