# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Exceptions handling (tr/except blocks).
# This is the exercise 10-7 which needs the exercise 10-5 done.
# -----------------------------------------------------------------------------
# 10-8:
# 1a. Make two files, cats.txt and dogs.txt.
# 1a.1. Store at least three names of cats in the first file
# 1a.2. and three names of dogs in the second file.
# 2a. Write a program that tries to read these files
# 2a.1. and print the contents of the file to the screen.
# 3a. Wrap your code in a try-except block
# 3a.1. to catch the FileNotFound error,
# 3a.2. and print a friendly message if a file is missing.
# 4a. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
# -----------------------------------------------------------------------------
from pathlib import Path

# -----------------------------------------------------------------------------

# 1a.
path_cats = Path("10_8_txt_files/cats.txt")

path_dogs = Path("10_8_txt_files/dogs.txt")

# 1a.1.
cats_print = "Indi"
cats_print += "\nAna"
cats_print += "\nJones"

try:  # 3a.
    path_cats.write_text(cats_print)
except FileNotFoundError:  # 3a.1
    print("--- Create the file cats.txt first. ---")  # 3a.2.

# 1a.2.
dogs_print = "Obi"
dogs_print += "\nWan-ke"
dogs_print += "\nNobi"

try:  # 3a.
    path_dogs.write_text(dogs_print)
except FileNotFoundError:  # 3a.1
    print("--- Create the file dogs.txt first. ---")  # 3a.2.


# 2a.
try:  # 3a.
    cats_names = path_cats.read_text()
    lines_cats = cats_names.splitlines()
    cats_names_list = ""
    for name in lines_cats:
        cats_names_list += name + "\n"
    print(cats_names_list)  # 2a.1.
except FileNotFoundError:  # 3a.1
    print("--- The file cats.txt does not exist! ---")  # 3a.2.

try:  # 3a.
    dogs_names = path_dogs.read_text()
    lines_dogs = dogs_names.splitlines()
    dogs_names_list = ""
    for name in lines_dogs:
        dogs_names_list += name + "\n"
    print(dogs_names_list)  # 2a.1.
except FileNotFoundError:  # 3a.1
    print("--- The file dogs.txt does not exist! ---")  # 3a.2.


# 4a. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.
