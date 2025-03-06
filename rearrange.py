import random
from python_quote import random_python_quote

def rearrange_words(sentence):
    words = sentence.split()  # Split sentence into words
    random.shuffle(words)  # Shuffle the words
    return ' '.join(words)  # Join words back into a sentence

if __name__ == '__main__':
    quote = random_python_quote()  # Get a random quote
    rearranged_quote = rearrange_words(quote)  # Rearrange words in the quote
    print(rearranged_quote)  # Print the rearranged quote
