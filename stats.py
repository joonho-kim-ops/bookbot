from collections import Counter

def word_count(text):
    words = text.split()
    num_words = len(words)
    return num_words

# Function to count letters in the text
# Not needed for main.py, but included for completeness
"""
def letter_count(text):
    letters = [char for char in text if char.isalpha()]
    num_letters = len(letters)
    return num_letters
"""
"""
def char_count(text):
    lower_text = text.lower()
    char_count = Counter(lower_text)
    return char_count

"""
# Manuel counter alternative
def char_count(text):
    chars = {}
    for char in text.lower():
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_char(char_dict):
    return dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
