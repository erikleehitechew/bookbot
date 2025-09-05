def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


# Write a main function that uses get_book_text
# with the relative path to your frankenstein.txt
# file to print the entire contents of the book to the console.

def main():

    book = get_book_text("./books/prideandprejudice.txt")
    print(book)

main()
