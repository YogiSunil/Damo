import re
from collections import defaultdict
import random

def build_markov_chain(file_path):
    """
    This function creates a third-order Markov chain from the input text. 
    It maps groups of three consecutive words to the word that follows them.
    """    
    markov_chain = defaultdict(list) # Dictionary to store the relationships

    with open(file_path, 'r', encoding='latin-1') as file:
        text = file.read().lower() 
        # Extract words from the text (ignoring punctuation)
        words = re.findall(r'\b\w+\b', text)

        # Build the Markov chain from word triplets
        for i in range(len(words) - 3):  # Iterate through the words (stop 3 words before the end)
            triplet = (words[i], words[i + 1], words[i + 2]) # Get three consecutive words
            markov_chain[triplet].append(words[i + 3]) # Link the triplet to the next word
    return markov_chain

def generate_sentence(markov_chain, num_words_to_generate):
    """
    Generates a random sentence using the Markov chain.
    Starts with three random words and keeps adding words based on the chain.
    """    
    triplets = list(markov_chain.keys())  # Get all groups of three words

    # Pick a random starting point (triplet)    
    current_triplet = random.choice(triplets)
    generated_words = [current_triplet[0], current_triplet[1], current_triplet[2]]

    # Keep adding words to the sentence
    for _ in range(num_words_to_generate - 3):  # Already have 3 words, so generate the rest
        successors = markov_chain.get(current_triplet, []) # Get the possible next words
        if not successors:  # If no successors exist, stop
            break  
        next_word = random.choice(successors) # Pick a random next word
        generated_words.append(next_word)  # Add the word to the sentence
        current_triplet = (current_triplet[1], current_triplet[2], next_word)  

    # Join the words into a single sentence
    sentence = " ".join(generated_words)

    # Capitalize the first letter and add a period at the end
    formatted_sentence = sentence.capitalize() + "."

    # Return the final sentence
    return formatted_sentence