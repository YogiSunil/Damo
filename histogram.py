from collections import Counter
import re


def histogram(source_text):
    """Takes text or filename, removes punctuation, and returns a word count dictionary."""
    with open('data/corpus.txt', 'r', encoding='utf-8') as file:
        source_text = file.read()

    # Step 1: Normalize punctuation like curly quotes to straight quotes
    source_text = source_text.replace('“', '"').replace('”', '"')
    source_text = source_text.replace('‘', "'").replace('’', "'")

    # Step 2: Tokenization using Regular Expressions to capture words and hyphenated words
    tokens = tokenize(source_text)

    # Step 3: Count word frequencies
    return Counter(tokens)

def tokenize(text):
    """Tokenizes the text into words, keeping hyphenated words and quotes as needed."""
    # Match words, hyphenated words, and words with quotes
    return re.findall(r'\b\w+(?:-\w+)*\b|\b"[^"]+"\b|\b\'[^\']+\'\b', text.lower())

def unique_words(histogram):
    """Returns the number of unique words in the histogram."""
    return len(histogram)

def frequency(word, histogram):
    """Returns how many times the word appears in the text."""
    return histogram.get(word.lower(), 0)

if __name__ == '__main__':
    hist = histogram('../data/corpus.txt')  

    print("words:", unique_words(hist))
    print("Frequency of 'words':", frequency('words', hist))
