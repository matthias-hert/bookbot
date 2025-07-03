
def count_word(text):
    words = text.split()
    return len(words)

def count_letters(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars [lowered] = 1
    return chars

def sort_on(items):
    return items["num"]

def pretty_report(chars):
    char_list = []
    for character in chars:
        char_dict = {"char":character, "num":chars[character]}
        char_list.append(char_dict)
    char_list.sort(reverse=True,key=sort_on)
    return char_list
        
