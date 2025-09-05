from collections import Counter
import string

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents

def remove_punc(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def word_counter(book):
    book = remove_punc(book).lower().split()

    word_counter = Counter(book)
    top25 = word_counter.most_common(25)

    sorted_var = sorted(word_counter.items(), key = lambda item: (-item[1], item[0]))

    #return sorted_var
    return top25

def main():
    #book = get_book_text("./books/frankenstein.txt")
    book = get_book_text("./books/preamble.txt")
    pairs = word_counter(book)
    
    for word, num in pairs:
        print(f"{word} : {(num)}")

main()
