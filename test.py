import random

test_string = "gjort blort hjort skort plunk slukk blunk klonk klort klart"

string_list = test_string.split()

#-
#testing my own ability to count to five and do addition and multiplication
#only took 2 tries! yay :/
# def letter_counter(tekst:str):
#     count = 0
#     for l in tekst:
#         if l == " ":
#             continue
#         else:
#             count += 1
#     print(count)
#     return count
#IT WORKS!

#-~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#random'ish 100 word gen
#ish as in i had a bad case of unimaginative writing the list of words, otherwise random

def r_word_gen(liste:list):
    rand_result = random.choices(liste, k=100)
    print(rand_result, len(rand_result))
    return rand_result
#- IT WORKS!

#-~~~~~~~~~~~~~~

def letter_dict_gen(sentence_split:list):
    text = " ".join(sentence_split)
    let_count = {}
    for l in text:
        if l not in let_count:
            let_count[l] = 0
        let_count[l] += 1
    return let_count

def sort_on(dict:dict):
    wide_d = [{"char":key, "num":value} for key, value in dict.items()]
    wide_d.sort(reverse=True, key=lambda x:x["num"])
    # print(wide_d[0]["num"])
    return wide_d

def forge_weapon(material):
    if material not in ["bronze", "iron", "steel"]:
        raise Exception("invalid material for weapon crafting")
    return f"{material} weapon"

def main():
    #letter_dict_gen(r_word_gen(string_list))
    sort_alg = sort_on(letter_dict_gen(string_list))
    for i in range(len(sort_alg)):
        print(f"letter- {sort_alg[i]['char']}: {sort_alg[i]['num']}")
    #letter_counter(test_string)
    
    #r_word_gen(string_list)

forge_weapon("gold")