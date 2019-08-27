"""
    all about alphabet is in here
"""

def in_list(alfabet, letter):
    if letter in alfabet:
        return alfabet.index(letter)

    return False


def get_letter(alfabet, begin, turns):
    i = 0
    indice = begin

    while(i < turns):
        if indice < (len(alfabet) - 1):
            indice = indice + 1
        elif indice == (len(alfabet) - 1):
            indice = 0

        i = i + 1

    return indice


def to_model(alfabet, word_map):
    word = []

    for i in word_map:
        word.append(alfabet[i])


    return word
