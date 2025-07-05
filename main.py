from stats import get_book_text
from stats import get_word_count
from stats import get_character_count
from stats import get_character_count_sorted
from pprint import pprint
import sys
def main ():
    """
    Main function to run the book text retrieval.
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    num_words = get_word_count(sys.argv[1])
  #  print(num_words, "words found in the document")
    num_characters = get_character_count(sys.argv[1])
 #   pprint(num_characters)
    sorted_characters = get_character_count_sorted(num_characters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("----------- Character Count -----------")
    for char in sorted_characters:
        print(char["char"] + ": " + str(char["count"]))
    print("===================================")
main()