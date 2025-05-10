def num_of_words(file_contents):
    word_count = 0
    for r in (file_contents.split()):
        word_count += 1
    return word_count

def num_of_char(file_contents):
    chars = {}
    file_contents = file_contents.lower()
    for c in file_contents:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sorted_list(chars):
    char_list = []  
    for c, r in chars.items():
        char_list.append({"char":c, "num":r})

    def sort_on(individual_dict):
        return individual_dict["num"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list 


