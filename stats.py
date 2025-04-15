PATH_TO_FILE = "books/frankenstein.txt"


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def word_count():
    text_from_file=get_book_text(PATH_TO_FILE)
    split_text = text_from_file.split()
    return len(split_text) -1
