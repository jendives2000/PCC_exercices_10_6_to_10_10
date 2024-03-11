
# WHAT I LEARNT

---

## The try/except Block

The **try/except block** was hard to grasp from the couple of videos I watched about it. None of them really mentioned the important role of **external 'sources'**, which mostly are: 
- user inputs, 
- project files 
- and network connections

And also try/except plays an important part in **securing the code**. As a developer, this is something to always keep in mind and watch out. 

Other than these points, the syntax is easy to use, nothing complicated here.  

And the error to pass after the `except` can easily be copy/pasted from the traceback error message.  

The other functionality of try/except is that it **can still be optional** even if used, with the `pass` method in the body of the except. 

![exercise 10-7](image-1.png)

Here the `pass` keeps the **error handling silent**. The user won't know about it, and he'd just keep on inputting numbers, even if only letters are typed in. 

---

## Read & Write

The `pathlib` library has methods like `read_text()` and `write_text()` that are self-explanatory. They are used with other methods to **manipulate contents of documents**. I played with the `.split()`, `splitlines()`, and `.count()` methods.  
The things that can be done with books and documents... 

### Beware of rewriting your file

The `write_text()` method, if the file it is writing on already exists, is constantly rewriting the file. So **be sure of your file names**, otherwise you **may be rewriting one of them** without knowing it. 

### The Importance of the Project's Folders Structure

But when working with these pathlib tools, the file path is essential. The **relative path** is for documents that are "close" to the project main files, meaning right in the same folder or one up.  
And if this is not a working option, then the **absolute path** will always works. 

--- 

## Fun with Books

This exercise 10-10 was fun. I searched for counts of given words in a book. 

I just watched a video about the philosopher Socrates (even if he did not consider himself a philosopher, or rather a 'wise man'.) And I learnt about this book named after a friend of him, and also the name of that book: Crito.  
Given the age of the book (about 2200 years old), I was pretty sure it was available in Gutenberg.org. 

Anyway, I knew the story of the book: his friend trying to help him escape. So I wanted to see how many times the word 'escape' appears in the book. To my disappointment, only 14 times. 

Of course I tried many other words: 

![fun with word counts in books](image-2.png)

--- 

## How Well Did I do?

After I compared my code to the solutions: 
- **exercise **:  
  Text 

  GRADE: Text. 

- **exercise **:  
  Text. 

- **exercise 10-8**:
  
  ![alt text](image.png)

#### Resources:
Python Crash Course 3rd Ed.: [solutions to exercises 8-8 to 8-10](https://ehmatthes.github.io/pcc_3e/solutions/chapter_8/#8-9-messages)  
Anaconda: [Forge package & icecream](https://anaconda.org/conda-forge/icecream)  
Github: [Icecream issues page](https://github.com/gruns/icecream/issues/79)
