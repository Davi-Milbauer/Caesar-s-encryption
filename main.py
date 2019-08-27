import sys
import string
from lib_alphabet import *

def create_word(message, letters_map):
    alphabet = list(string.ascii_lowercase)
    alphabet.reverse()

    indices = []

    message_length = len(message)

    for i in range(message_length):
        found = in_list(alphabet, message[i])

        if not found:
            print("The Letter isnt found!\n")
            sys.exit(1)
        else:
            indices.append(found)

    word_map = []
    j = 0

    for i in indices:
        new_letter = get_letter(alphabet, i, letters_map[j])
        word_map.append(new_letter)
        j = j + 1


    if not word_map:
        print("error to create word!\n")


    # model the word using alphabet indices
    word = to_model(alphabet, word_map)

    return ''.join(word)

def let_integer(element):
    return int(element)


def model_line(line, identifier):
    #modifica a linha de inteiros digitados pelo usuario
    #para criar um mapa

    single_strings = line.split()

    numbers = []

    for element in single_strings:
        new_item = element.split(identifier)
        numbers.append(new_item)

    return numbers


def main():
    file_message = open("resource/text.txt")
    message = file_message.readline()
    single_words = message.split()

    file_message.close()

    file_keys = open("resource/keys.txt")
    keys = file_keys.readline()

    file_keys.close()

    char_numbers = model_line(keys, "-")
    letters_map = []

    for i in char_numbers:
        new_list = list(map(let_integer, i))
        letters_map.append(new_list)


    print("found map: ")
    print(letters_map)
    print("\n\n\n")

    word = []
    j = 0

    for i in single_words:
        new_word = create_word(i, letters_map[j])
        j = j + 1
        word.append(new_word)


    print("The found message its: ", end="")

    phrase = ' '.join(word)
    print(phrase)


if __name__ == "__main__":
    main()
