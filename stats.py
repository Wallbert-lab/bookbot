import sys
system_arguments = sys.argv


def sys_test(arguments:list):
    if len(arguments) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    return sys.argv

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read() #returns string object


def word_count():
    text_from_file=get_book_text(system_arguments[1])
    split_text = text_from_file.split()
    return len(split_text) -1

def letter_count(f_path:str):
    text_string = get_book_text(f_path).lower()
    letter_dict = {}
    
    for l in text_string: #looping through text_string
        if l not in letter_dict and l.isalpha(): #checks if letter is in the dict and is a letter
            letter_dict[l] = 0 #if not is added with the value 0
        elif l.isalpha() != True:
            continue
        letter_dict[l] += 1
    return letter_dict

def sort_on(dict:dict):
    wide_d = [{"char":key, "num":value} for key, value in dict.items()]
    wide_d.sort(reverse=True, key=lambda x:x["num"])
    return wide_d

