import sys
import random

"""
-Write the dictonary_words.py script:
-read in the words file
-select a random set of words from the file and store in a data type
-put the number of words requested together into a “sentence”
-output your sentence

"""


def random_set(number):
    """Open file and read the words. Remove extra space from word list. Select number of random words. 
    Join words into a sentence and add a period at the end. 
    """
    with open('/usr/share/dict/words', 'r') as file:
        words = file.readlines()  
    words = [word.strip() for word in words]
    random_words = random.sample(words, number)  
    sentence = ' '.join(random_words) + '.'  
    return sentence  


if __name__ == "__main__":
    number = int(sys.argv[1])
    print(random_set(number))