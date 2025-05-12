def get_book_text():
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        splitted = contents.split()
        length = len(splitted)
        print(f"{length} words found in the document")

def occurences():
    count = {}
    with open("./books/frankenstein.txt") as f:
        contents = f.read()
        lowered_contents = contents.lower()
        for char in lowered_contents:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        print(count)