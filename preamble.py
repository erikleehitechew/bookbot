import string

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


# Write a main function that uses get_book_text
# with the relative path to your frankenstein.txt
# file to print the entire contents of the book to the console.

def main():

    book = get_book_text("./books/preamble.txt")
    
    words = book.split()
    unique_words = list(set(words))

    #print(words)

    print(f"Number of words total: {len(words)}")
    print(f"Number of unique words: {len(unique_words)}")

    sorted_list = sorted(words)
    descended = sorted(words,reverse = True)

    words_displayed = []

    translator = str.maketrans('', '', string.punctuation)

    for item in sorted_list:
        item = item.translate(translator)
        if item not in words_displayed:
            print(str(item) + ": " + str(sorted_list.count(item)) + " occurrences")
            words_displayed.append(item)

main()
