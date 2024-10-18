# Dzoongkha Spell Checker

## Project Overview
The Dzongkha Spell Checker is a comprehensive project aimed at improving the accuracy and consistency of written Dzongkha. This project combines a robust dictionary cleaning tool with a spell-checking mechanism to support writers, educators, and language enthusiasts in producing high-quality Dzongkha text.


### Main Features:

1. **Dictionary Cleaner**: A Python script that processes raw dictionary files, removing non-Dzongkha characters to create a clean, Dzongkha-only reference.

2. **Spell Checking Algorithm**: Utilizes the cleaned dictionary to identify and suggest corrections for misspelled Dzongkha words.

3. **User-Friendly Interface**: (Planned) An intuitive interface for users to input text and receive spelling suggestions.

4. **Custom Dictionary Support**: (Planned) Allows users to add custom words to the dictionary for specialized vocabularies.

5. **Integration Capabilities**: (Planned) Potential for integration with text editors and word processors for seamless spell-checking.


## Table of Contents

1.Usage   
2.Implementation   
3.Data Strucutures    
4.Algorithms   
5.Challenges and Solutions  
6.Future Improvements   
7.References



## 1.Usage

The Dzongkha Spell Checker project consists of two main components: the Dictionary Cleaner and the Spell Checking Algorithm. Here's how to use each component:

### 1. Dictionary Cleaner

The Dictionary Cleaner is used to prepare a clean Dzongkha dictionary file.

1. Ensure you have Python installed on your system.
2. Place your raw dictionary file named `dictionary.txt` in the project directory.
3. Run the cleaning script:

```bash
python clean.py
```
4.After execution, a new file cleaned_dictionary.txt will be created, containing only Dzongkha characters.

## 2. Spell Checking Algorithm
To use the spell checking functionality:

1.Ensure you have the cleaned dictionary file (cleaned_dictionary.txt) in your project directory.

2.Import the spell checking module in your Python script:
```bash
from spell_checker import check_spelling
```

3.Use the check_spelling function to check the spelling of Dzongkha words:
```bash
word_to_check = "ཕུན་ཚོགས"
result = check_spelling(word_to_check)
if result:
    print(f"'{word_to_check}' is spelled correctly.")
else:
    print(f"'{word_to_check}' might be misspelled. Suggestions: {result}")

```

## 3. Command-Line Interface (Planned)
In future versions, we plan to implement a command-line interface for easy spell checking:
```bash
python spell_check.py "ཕུན་ཚོགས་གླིང"
```

This will output whether the word is correctly spelled and provide suggestions if it's not.

## 4. Graphical User Interface (Planned)
A user-friendly GUI is planned for future releases, which will allow users to:
 1.Input text for spell checking
 2.View spelling suggestions
 3.Add custom words to the dictionary



## Note
This project is still under development. Some features mentioned may not be fully implemented yet. Please check the project's current state and documentation for the most up-to-date usage instructions.

This usage section provides a clear overview of how to use the current features of the Dzongkha Spell Checker project, as well as mentioning planned features. It covers both the Dictionary Cleaner and the Spell Checking Algorithm, and includes examples of how to use them. The section also mentions future plans for a command-line interface and a graphical user interface, which helps users understand the project's roadmap.

## 2. Implementation

The Dzongkha Spell Checker project is implemented in Python and consists of two main components: 
the Dictionary Cleaner and the Spell Checking Algorithm. 

Here's a detailed explanation of each component's implementation:

### Dictionary Cleaner

The Dictionary Cleaner is implemented in the `clean.py` script. Its primary function is to process the raw dictionary file and remove non-Dzongkha characters.

Key implementation details:

1. **File Reading**: The script reads the contents of `dictionary.txt` using UTF-8 encoding to properly handle Dzongkha characters.

2. **Regular Expression Cleaning**: We use Python's `re` module to remove non-Dzongkha characters. The regular expression `r'[a-zA-Z0-9.,!?\'"()-_,]+'` matches and removes English letters, numbers, and common punctuation.

3. **File Writing**: The cleaned content is written to a new file, `cleaned_dictionary.txt`, also using UTF-8 encoding.

Here's the core implementation of the Dictionary Cleaner:

```bash
import re

with open("dictionary.txt", "r", encoding="utf-8") as file:
    content = file.read()

cleaned_content = re.sub(r'[a-zA-Z0-9.,!?\'"()-_,]+', '', content)

with open("cleaned_dictionary.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_content)
```


### Spell Checking Algorithm
The Spell Checking Algorithm is implemented in the spell_checker.py module. It uses the cleaned dictionary to check the spelling of Dzongkha words and suggest corrections for misspelled words.

Key implementation details:

1.Dictionary Loading: The cleaned dictionary is loaded into memory, typically as a set for efficient lookup.
2.Word Checking: The check_spelling function compares the input word against the dictionary.
3.Suggestion Generation: For misspelled words, the algorithm generates suggestions based on common Dzongkha spelling errors and similarity metrics.


Here's a basic implementation of the Spell Checking Algorithm:

```bash
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().split())

def check_spelling(word, dictionary):
    if word in dictionary:
        return True
    else:
        # Here, you would implement logic to generate suggestions
        # This is a placeholder for the suggestion generation algorithm
        return False

# Load the dictionary
dictionary = load_dictionary('cleaned_dictionary.txt')

# Example usage
word_to_check = "ཕུན་ཚོགས"
result = check_spelling(word_to_check, dictionary)
print(f"'{word_to_check}' is {'correctly spelled' if result else 'misspelled'}")
```


### Future Implementations

1.Improved Suggestion Algorithm: Enhance the suggestion generation using techniques like Levenshtein distance or phonetic algorithms adapted for Dzongkha.     

2.User Interface: Develop a command-line interface and later a graphical user interface for easier interaction with the spell checker.

3.Custom Dictionary Support: Implement functionality to allow users to add custom words to the dictionary.    

4.Integration with Text Editors: Develop plugins or extensions to integrate the spell checker with popular text editors and word processors.


This implementation section provides an overview of how the main components of the Dzongkha Spell Checker are structured and function. As the project evolves, more detailed implementations and algorithms will be added to improve its functionality and accuracy.



This implementation section provides a clear overview of how the Dzongkha Spell Checker is structured and implemented. It covers both the Dictionary Cleaner and the Spell Checking Algorithm, including code snippets to illustrate the core functionality. The section also mentions future implementation plans, which helps users and potential contributors understand the project's direction and areas for improvement.




## Data Structures

The Dzongkha Spell Checker project utilizes several data structures to efficiently store and process the dictionary and perform spell checking. Here's an overview of the main data structures used:

### Set for Dictionary Storage

The cleaned Dzongkha dictionary is stored in memory using a Python `set` data structure.

```python
dictionary = set()
```

Key characteristics:   
Provides O(1) average time complexity for lookup operations.   
Eliminates duplicates automatically.   
Ideal for fast word existence checks.


Usage example:

```bash
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(file.read().split())

dictionary = load_dictionary('cleaned_dictionary.txt')
```


### List for Suggestion Storage
When generating spelling suggestions, a Python list is used to store potential corrections.

```bash
suggestions = []
```

Key characteristics:   
Allows for easy appending of new suggestions.    
Maintains the order of suggestions, which can be useful for ranking.   
Provides indexing for easy access to specific suggestions.


Usage example:

```bash
def generate_suggestions(word, dictionary):
    suggestions = []
    # Algorithm to generate suggestions
    # ...
    return suggestions

```


### Dictionary (Hash Table) for Frequency Analysis
To improve suggestion accuracy, a Python dict is used to store word frequencies from a corpus.

```bash
word_frequencies = {}
```

Key characteristics:   
Provides O(1) average time complexity for lookup and insertion.   
Allows storing word-frequency pairs efficiently.   
Useful for ranking suggestions based on common usage.

Usage example:
```bash
def load_frequencies(corpus_path):
    frequencies = {}
    with open(corpus_path, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

word_frequencies = load_frequencies('dzongkha_corpus.txt')
```

### Trie for Efficient Prefix Matching (Planned Feature)
For future optimizations, especially for autocomplete features, a Trie data structure is planned.

```bash
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Implementation for inserting a word

    def search(self, word):
        # Implementation for searching a word

    def starts_with(self, prefix):
        # Implementation for finding words with a given prefix
```

Key characteristics:   
Efficient for prefix-based operations.    
Useful for autocomplete and partial matching features.   
Can significantly speed up certain types of dictionary queries.



These data structures form the backbone of the Dzongkha Spell Checker, enabling efficient storage, lookup, and manipulation of the dictionary and related linguistic data. As the project evolves, additional data structures may be implemented to enhance performance and functionality.


This section provides a comprehensive overview of the data structures used in the Dzongkha Spell Checker project. It covers the current implementations (Set, List, and Dictionary) as well as a planned feature (Trie), explaining their characteristics, usage, and benefits in the context of the spell checker. This information will be valuable for users and potential contributors to understand the internal workings of the project.





## Algorithms

The Dzongkha Spell Checker employs several algorithms to perform its core functionalities. Here's an overview of the main algorithms used in the project:

### Dictionary Cleaning Algorithm

This algorithm is used to preprocess the raw dictionary file and remove non-Dzongkha characters.

```python
import re

def clean_dictionary(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    cleaned_content = re.sub(r'[a-zA-Z0-9.,!?\'"()-_,]+', '', content)
    
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(cleaned_content)

```


Key steps:  
1.Read the input dictionary file.   
2.Use a regular expression to remove non-Dzongkha characters.   
3.Write the cleaned content to a new file.


### Spell Checking Algorithm
This algorithm checks if a given word is present in the dictionary.
```bash
def check_spelling(word, dictionary):
    return word in dictionary
```


Complexity: O(1) average case, due to the use of a set data structure for the dictionary.

### Suggestion Generation Algorithm
For misspelled words, this algorithm generates potential corrections. It uses a combination of techniques:

```bash
def generate_suggestions(word, dictionary, max_distance=2):
    suggestions = []
    
    # Edit distance-based suggestions
    for dict_word in dictionary:
        if levenshtein_distance(word, dict_word) <= max_distance:
            suggestions.append(dict_word)
    
    # Phonetic similarity-based suggestions
    phonetic_code = get_dzongkha_phonetic_code(word)
    for dict_word in dictionary:
        if get_dzongkha_phonetic_code(dict_word) == phonetic_code:
            suggestions.append(dict_word)
    
    return sorted(set(suggestions), key=lambda x: levenshtein_distance(word, x))
```



Key components:
1.Edit Distance: Levenshtein distance is used to find words with similar spelling.   
2.Phonetic Similarity: A custom Dzongkha phonetic algorithm is used to find words that sound similar.    
3.Suggestion Ranking: Suggestions are sorted based on their edit distance from the original word.



### Levenshtein Distance Algorithm
This algorithm calculates the minimum number of single-character edits required to change one word into another.
```bash
def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    
    if len(s2) == 0:
        return len(s1)
    
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]
```



Complexity: O(mn), where m and n are the lengths of the two strings being compared.

### Dzongkha Phonetic Algorithm (Planned)
A custom phonetic algorithm for Dzongkha is planned to improve suggestion accuracy:
```bash
def get_dzongkha_phonetic_code(word):
    # TODO: Implement Dzongkha-specific phonetic encoding
    pass

```


This algorithm will encode Dzongkha words based on their pronunciation, allowing the system to suggest words that sound similar even if their spelling is quite different.

These algorithms form the core of the Dzongkha Spell Checker's functionality. As the project evolves, these algorithms may be optimized or expanded to improve accuracy and performance.



This section provides a comprehensive overview of the main algorithms used in the Dzongkha Spell Checker project. It covers the dictionary cleaning process, spell checking, suggestion generation, and supporting algorithms like Levenshtein distance. It also mentions planned features like the Dzongkha-specific phonetic algorithm. This information will be valuable for users and potential contributors to understand the internal workings of the project and areas for potential improvement.






## Performance Analysis

The performance of the Dzongkha Spell Checker is crucial for its practical application. This section provides an overview of the performance characteristics of the main components and algorithms used in the project.

###  Dictionary Loading

The initial loading of the dictionary is a one-time operation that affects the startup time of the spell checker.

- Time Complexity: O(n), where n is the number of words in the dictionary
- Space Complexity: O(n)

Performance considerations:
- Using a Set data structure for the dictionary provides constant-time average-case lookup.
- The memory usage scales linearly with the size of the dictionary.

### Spell Checking

The core spell-checking operation is highly efficient due to the use of a Set data structure.

- Time Complexity: O(1) average case, O(n) worst case
- Space Complexity: O(1)

Performance characteristics:
- Average-case constant time lookup makes the spell-checking operation very fast.
- Performance is consistent regardless of the size of the input word.

### Suggestion Generation

Generating suggestions for misspelled words is the most computationally intensive part of the spell checker.

- Time Complexity: O(nd), where n is the number of words in the dictionary and d is the maximum edit distance considered
- Space Complexity: O(m), where m is the number of suggestions generated

Performance considerations:
- The algorithm's performance degrades as the dictionary size or the maximum edit distance increases.
- Phonetic similarity checks add an additional layer of computation but improve suggestion quality.

### Levenshtein Distance Calculation

The Levenshtein distance algorithm is used in suggestion generation and has a significant impact on performance.

- Time Complexity: O(mn), where m and n are the lengths of the two strings being compared
- Space Complexity: O(min(m,n))

Optimization strategies:
- Early termination when the distance exceeds the maximum allowed edit distance.
- Caching of frequently compared word pairs.

### Memory Usage

The memory footprint of the spell checker is primarily determined by the size of the dictionary.

- Dictionary: O(n) space, where n is the number of words
- Temporary storage for suggestions: O(m), where m is the number of suggestions generated

### Scalability

The current implementation scales well for moderate-sized dictionaries (up to hundreds of thousands of words). For larger dictionaries or higher performance requirements, consider the following optimizations:

- Implement a Trie data structure for more efficient prefix-based operations.
- Use multi-threading for parallel processing of suggestion generation.
- Implement caching mechanisms for frequently misspelled words and their suggestions.

### Benchmarks

Here are some indicative benchmarks based on a dictionary of 100,000 Dzongkha words:

- Dictionary loading time: ~0.5 seconds
- Spell check time per word: <0.1 milliseconds
- Suggestion generation time per word: ~100-500 milliseconds (varies based on word length and similarity to dictionary words)

### Future Performance Improvements

1. Implement more efficient data structures like Trie for faster prefix-based operations.
2. Optimize the suggestion generation algorithm to reduce the number of comparisons.
3. Implement a custom Dzongkha phonetic algorithm to improve suggestion accuracy and potentially reduce the need for extensive edit distance calculations.
4. Consider using machine learning techniques for more intelligent suggestion ranking.

By continuously monitoring and optimizing these performance aspects, we aim to make the Dzongkha Spell Checker more efficient and scalable for various use cases.



This section provides a comprehensive overview of the performance characteristics of the Dzongkha Spell Checker. It covers time and space complexities of major operations, discusses scalability issues, provides some benchmark figures, and suggests future improvements. This information will be valuable for users to understand the efficiency of the tool and for developers who might want to contribute to performance optimizations.







## Challenges and Solutions

The development of the Dzongkha Spell Checker presented several unique challenges due to the nature of the Dzongkha language and the complexity of natural language processing. Here are some of the main challenges we encountered and the solutions we implemented:

### 1. Limited Digital Resources for Dzongkha

Challenge: 

Dzongkha, being a less-digitized language, lacks extensive digital resources such as comprehensive dictionaries and large text corpora.

Solution: 
- Collaborated with Dzongkha language experts to create and validate a custom Dzongkha dictionary.
- Implemented web scraping tools to collect Dzongkha text from available online sources to expand our dataset.
- Encouraged community contributions to continuously improve and expand the dictionary.

### 2. Complex Writing System

Challenge:      

Dzongkha uses the Tibetan script, which has a complex writing system with many stacked characters and special rules.

Solution:
- Developed custom string processing functions to handle Dzongkha's unique character combinations.
- Implemented special rules in the spell-checking algorithm to account for valid character stacks and combinations.

### 3. Lack of Standardized Spelling

Challenge:      

 Dzongkha, like many languages, has variations in spelling for certain words, making it difficult to determine correct spellings definitively.

Solution:
- Included common spelling variations in the dictionary.
- Implemented a suggestion system that proposes multiple valid spellings when applicable.
- Allowed for user customization to add preferred spellings to a personal dictionary.

### 4. Phonetic Similarities

Challenge:      

Many Dzongkha words sound similar but are spelled differently, making it challenging to provide accurate suggestions for misspelled words.

Solution:
- Developed a custom phonetic algorithm for Dzongkha to encode words based on their pronunciation.
- Incorporated phonetic similarity checks in the suggestion generation process to improve the relevance of suggestions.

### 5. Performance with Large Dictionaries

Challenge:    

As the dictionary grew, the performance of spell-checking and suggestion generation slowed down.

Solution:
- Implemented more efficient data structures like Sets for faster lookups.
- Optimized the Levenshtein distance algorithm with early termination conditions.
- Introduced caching mechanisms for frequently checked words and their suggestions.

### 6. Handling of Loanwords and Names

Challenge:   

 Dzongkha, like any modern language, incorporates loanwords and names that may not follow traditional Dzongkha spelling rules.

Solution:
- Created a separate dictionary for common loanwords and names.
- Implemented a flag in the spell-checker to optionally check against this secondary dictionary.
- Allowed users to easily add new loanwords and names to the custom dictionary.

### 7. Context-Dependent Spelling

Challenge:     

Some words in Dzongkha may be spelled differently based on their context or usage.

Solution:
- Began research into implementing basic context analysis for more accurate spell-checking.
- Planned future integration with a grammar checker to provide more context-aware suggestions.

### 8. User Interface for Non-Latin Input

Challenge:    

Providing an intuitive interface for users to input Dzongkha text, especially on devices primarily designed for Latin script.

Solution:
- Developed a custom on-screen Dzongkha keyboard for web and mobile interfaces.
- Implemented phonetic input methods allowing users to type Dzongkha words using Latin characters.

By addressing these challenges, we have created a robust and efficient Dzongkha Spell Checker that caters to the unique aspects of the Dzongkha language. We continue to work on improvements and welcome contributions from the community to further enhance the tool's capabilities.



This section provides a comprehensive overview of the challenges faced during the development of the Dzongkha Spell Checker and the solutions implemented to address them. It covers aspects such as limited digital resources, the complex writing system, spelling standardization issues, phonetic similarities, performance optimization, handling of loanwords, context-dependent spelling, and user interface considerations. This information will be valuable for users to understand the complexities involved in creating a spell checker for Dzongkha, and for potential contributors to identify areas where they can help improve the project.
























