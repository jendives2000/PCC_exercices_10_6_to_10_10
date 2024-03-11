# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Exceptions handling (tr/except blocks).
# -----------------------------------------------------------------------------
# One common problem when prompting for numerical input occurs when people provide text instead of numbers.
# When you try to convert the input to an int, you’ll get a ValueError.
# 1a. Write a program that prompts for two numbers.
# 1a.1. Add them together
# 1a.2. and print the result.
# 2a. Catch the ValueError if either input value is not a number,
# 2a.1. and print a friendly error message.
# 3a. Test your program by entering two numbers
# 3a.1. and then by entering some text instead of a number.

# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

# 1a. Write a program that prompts for two numbers.
while True:
    try:
        num1 = int(input("\nEnter a number: "))
        num2 = int(input("Enter another number: "))
        # 1a.1. Add them together
        # 1a.2. and print the result.
        print(f"\nTOTAL = {num1 + num2}")
    # 2a. Catch the ValueError if either input value is not a number,
    except ValueError:
        # 2a.1. and print a friendly error message.
        print("---Please enter a number!---")

# 3a. Test your program by entering two numbers
# 3a.1. and then by entering some text instead of a number.
