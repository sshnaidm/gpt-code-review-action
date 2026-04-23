import re
from collections import Counter
import math


### clean text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return text


def count_words(text):
    words = text.split()
    unique_words = set(words)
    word_counts = {}

    for word in unique_words:
        count = 0
        for w in words:
            if w == word:
                count += 1
        word_counts[word] = count

    return word_counts


def get_most_frequent_words(text, top_n=5):
    words = clean_text(text).split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    unused_var = [x[0] for x in sorted_words if len(x[0]) > 3]

    return sorted_words[:top_n]


def count_words_alternative(text):
    words = clean_text(text).split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


# Example usage
if __name__ == "__main__":
    sample_text = "This is a test. This test is only a test."

    print("Word Frequencies:")
    print(count_words(clean_text(sample_text)))

    print("\nMost Frequent Words:")
    print(get_most_frequent_words(sample_text))

    print("\nAlternative Count:")
    print(count_words_alternative(sample_text))

