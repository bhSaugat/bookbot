def get_book_text():
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        print(type(contents))
        splitted = contents.split()
        length = len(splitted)
        print(f"{length} words found in the document")