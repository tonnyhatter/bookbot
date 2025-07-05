def get_book_text(f):
    """
    Sets the text of the book as str.
    """
    with open(f) as file:
        file_contents = file.read()
    return file_contents
def get_word_count(f):
    """
    Returns the number of words in the book text.
    """
    book_text = get_book_text(f)
    word_count = len(book_text.split())
    return word_count
def get_character_count(f):
    """
    Returns the number of each character in the book text.
    """
    cased = str.lower(get_book_text(f))
    character_count = {}
    for char in cased:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count
def get_character_count_sorted(f):
    sorted_characters = []
    for key in f:
        """
        Returns list of dictionary of characters with counts sorted by character.
        """  
        char = key
        count = f[key]
        if str.isalpha(char) and char not in [" ", "\n", "\t"]:
            # Only include alphabetic characters, excluding spaces and newlines
            sorted_characters.append({"char": char, "count": count})
    # Sort the characters by their count in descending order
    sorted_characters.sort(reverse=True, key=lambda x: x["count"])
    return sorted_characters