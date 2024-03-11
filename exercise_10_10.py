# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Exceptions handling (tr/except blocks).
# -----------------------------------------------------------------------------
# Visit Project Gutenberg (https://gutenberg.org ) and find a few texts you’d like to analyze

# -----------------------------------------------------------------------------
from pathlib import Path

# -----------------------------------------------------------------------------

# read the book "Crito" and store the data in read_book
path_crito = Path("10_10_book_files/crito_by_plato.txt")

try:
    read_book = path_crito.read_text(encoding="utf8")
except FileNotFoundError:
    print("--- The book crito_by_plato.txt does not exist! ---")

# total number of words:
words = read_book.split()  # list of all words
total_word_count = len(words)
print(f"\nThe book has:\n\t{total_word_count} words.\n")

# all words joined in one variable
words_joined = "".join(words)


def word_appear_count(*words):
    for word in words:
        # number of instances of a word
        number_of_word = words_joined.lower().count(word)
        print(f'In this book the word:\n\t"{word}" appeared {number_of_word} times.')


word_appear_count(
    "crito",
    "escape",
    "socrates",
    "plato",
    "law",
    "judge",
    "punishment",
    "justice",
    "athens",
    "athenians",
    "god",
    "wise",
)
