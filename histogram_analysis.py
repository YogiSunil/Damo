# histogram_analysis.py

from histogram import histogram, unique_words, frequency
import timeit
from collections import Counter  # Import Counter here

def analyze_histogram(file_path):
    # Create histogram from the source text file
    hist = histogram(file_path)

    # Display results
    print("Unique words:", unique_words(hist))
    print("Frequency of 'castle':", frequency('castle', hist))

    # Benchmarking frequency lookups
    words_to_test = ['castle', 'the', 'and', 'notfoundword']  # Example words for testing
    iterations = 10000

    # Create a string for the setup code to include hist
    setup_code = f"""
from histogram import frequency
from collections import Counter  # Make sure Counter is also imported
hist = {hist}  # Use the histogram directly
"""

    for word in words_to_test:
        stmt = f"frequency('{word}', hist)"
        timer = timeit.Timer(stmt, setup=setup_code)
        result = timer.timeit(number=iterations)

        print(f"Time to find '{word}' in histogram for {iterations} iterations: {result}")


if __name__ == "__main__":
    analyze_histogram('data/corpus.txt')  # Make sure this path is correct
