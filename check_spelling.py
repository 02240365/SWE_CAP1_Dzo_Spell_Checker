def check_spelling(word, dictionary_file):
    """
    Check if a word is in the dictionary file.
    
    Args:
    word (str): The word to search for.
    dictionary_file (str): Path to the dictionary file.
    
    Returns:
    bool: True if the word is in the dictionary, False otherwise.
    """
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        for line in file:
            if word.strip() == line.strip():
                return True
    return False

# Usage example
dictionary_file = 'cleaned_dictionary.txt'  # Use the path to your cleaned dictionary file
word_to_check = 'ཐིམ་ཕུག' # Replace with the word you want to check

if check_spelling(word_to_check, dictionary_file):
    print(f"'{word_to_check}' is in the dictionary.")
else:
    print(f"'{word_to_check}' is not in the dictionary.")

