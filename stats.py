def get_word_count(text):
    words = text.split()
    word_count = len(words)
    return word_count

def get_char_count(text):
    lowercase = text.lower()
    char_counts = {}
    for i in lowercase:
        letter = i
        if letter in char_counts:
            char_counts[letter] += 1
        else:
            char_counts[letter] = 1
    return char_counts

def sort_char(character):
    return character["char"]
def sort_num(number):
    return number["num"]

def sort_dict(dictionary):
    char_list = []
    for char, num in dictionary.items():
        charnum_list = {"char": char, "num": num}
        char_list.append(charnum_list)
    char_list.sort(reverse=True, key=sort_num)
    return char_list