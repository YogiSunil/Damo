import re
import sys
from collections import defaultdict

def read_text_file(filepath):
    """Read the text file and return its contents as a string."""
    with open(filepath, 'r') as file:
        return file.read()

def histogram(source_text):
    """Create a histogram from the source text."""
    words = re.findall(r'\b\w+\b', source_text.lower())
    hist = defaultdict(int)
    for word in words:
        hist[word] += 1
    return hist

def unique_words(hist):
    """Return the total count of unique words in the histogram."""
    return len(hist)

def frequency(word, hist):
    """Return the number of times the word appears in the histogram."""
    return hist.get(word.lower(), 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 word_frequency.py <text_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    source_text = read_text_file(filepath)
    hist = histogram(source_text)

    print(f"Total unique words: {unique_words(hist)}")
    print(f"Frequency of 'the': {frequency('the', hist)}")
    print(f"Frequency of 'and': {frequency('and', hist)}")