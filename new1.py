def beautify_text(text: str) -> str:
    """
    A utility function to enhance the appearance of text by capitalizing 
    each word and adding some visual flair.
    """
    return f"{text.capitalize()}"

def sort_and_remove_duplicates(words: list) -> list:
    """
    Sorts the list of words alphabetically and removes duplicates.
    """
    return sorted(set(words))

def print_sorted_words(words: list) -> None:
    """
    Prints the sorted and unique words in a visually appealing format.
    """
    print("\nHere are the unique and sorted words in style:\n")
    
    # Beautifying the header
    print(beautify_text("Sorted and Unique Words"))
    print("-" * 40)

    # Iterating through the words and printing them beautifully
    for word in words:
        print(f"{word.capitalize()}")

# Sample list of words with duplicates and unordered
word_list = [
    "apple", "banana", "Orange", "grape", "Apple", "banana", "Peach", "grape", "pear"
]

# Removing duplicates, sorting the list and printing the result
sorted_unique_words = sort_and_remove_duplicates(word_list)
print_sorted_words(sorted_unique_words)
