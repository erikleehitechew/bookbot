from stats import get_num_words, char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


# Write a main function that uses get_book_text
# with the relative path to your frankenstein.txt
# file to print the entire contents of the book to the console.

def main():

    #book = get_book_text("./books/frankenstein.txt")
    #print(f"{len(book.split())} words found in the document")
    
    #print(f"{len(sys.argv)} is the number of arguments")

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])

    get_num_words(book)

    char_count(book)
    

main()
