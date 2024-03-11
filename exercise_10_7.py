# Exercises from the book Python Crash Course by Eric Matthes.
# These exercises are about Exceptions handling (tr/except blocks).
# This is the exercise 10-7 which needs the exercise 10-5 done.
# -----------------------------------------------------------------------------
# 10-7:
# Continue with your code from Exercise 10-6
# 2a. so the user can continue entering numbers, even if they make a mistake and enter text instead of a number.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

while True:
    try:
        num_1 = int(input("\nEnter a number: "))
        num_2 = int(input("Enter another number: "))
        print(f"\nTOTAL = {num_1 + num_2}")
    except ValueError:
        pass  # 2a.
