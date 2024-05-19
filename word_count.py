import re

def count_words(text):
    # Use regular expression to split the text by non-word characters
    words = re.findall(r'\b\w+\b', text)
    # Count the number of words
    num_words = len(words)
    return num_words

# Directly call the function for user input and output
text = input("Enter a text: ")
word_count = count_words(text)
print(f"The number of words in the text is: {word_count}")