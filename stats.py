def get_book_text(text_path):
    with open(text_path) as f:
        contents = f.read()
        splitted = contents.split()
        length = len(splitted)
        """ print(f"{length} words found in the document") """
        return length
def occurences(text_path):
    count = {}
    with open(text_path) as f:
        contents = f.read()
        lowered_contents = contents.lower()
        for char in lowered_contents:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        """ print(count) """
    return count

""" def sorted_chars(dict):
    collected_chars = []
    tmp_dict = {}
    for key, value in dict.items():
        if key.isalpha():
            tmp_dict = {"char": key, "num": value}
            collected_chars.append(tmp_dict)
    sorted_people = sorted(collected_chars, key=lambda x: x['char'])
    print(sorted_people) """

def listed_chars(dict):
    collected_chars = []
    tmp_dict = {}
    for key, value in dict.items():
        if key.isalpha():
            tmp_dict = {"char": key, "num": value}
            collected_chars.append(tmp_dict)
    return collected_chars

def sort_on(dict):
    return dict["num"]