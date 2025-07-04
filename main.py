from stats import get_book_text
from stats import get_word_count
from stats import get_character_count
from pprint import pprint
def main ():
    """
    Main function to run the book text retrieval.
    """
    num_words = get_word_count("books/frankenstein.txt")
    print(num_words, "words found in the document")
    num_characters = get_character_count("books/frankenstein.txt")
    pprint(num_characters)
main()