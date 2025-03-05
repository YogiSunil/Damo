"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from markov import build_markov_chain, generate_sentence
import os

app = Flask(__name__)

# Initialize the Markov chain when the server starts
markov_chain = build_markov_chain("data/corpus.txt")

@app.route("/")
def home():
    """Generate a sentence using the Markov chain."""
    num_words_to_generate = 8
    sentence = generate_sentence(markov_chain, num_words_to_generate)
    return render_template("index.html", sentence=sentence)
    
if __name__ == "__main__":
    app.run(debug=True)
