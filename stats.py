from collections import Counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def sort_on(items):
    return items["num"]

# Write a main function that uses get_book_text
# with the relative path to your frankenstein.txt
# file to print the entire contents of the book to the console.

def get_num_words(book):

    #book = get_book_text("./books/frankenstein.txt")
    print('''============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------''')
    print(f"Found {len(book.split())} total words")
    print("--------- Character Count -------")



def char_count(book: str) -> dict[str, int]:
    # Take text from book as string
    # return number of times each character, lowercase,
    # including symbols and spaces, appears in the string

    results = dict(Counter(book.lower()))
    
    results = sorted(results.items(), key = lambda x: (-x[1], x[0]))

    for char, tally in results:
        if char.isalpha():
            print(f"{char}: {tally}")
