# ':n', ':e', ':s', ':w', ':m', ':b', ':d', ':a', ':N', ':E', ':S', ':W', ':M', ':B', ':D', ':A'
# N, E, S, W, M(NE), B(NW), D(SE), A(SW)

import sys
from utils.keyboard_dictionary import *
from utils.dictionary_words import dictionary_word

def keyboard_walk(password):
    global letters

    path = ''
    start_index = None
    for i in range(len(password)-1):
        current_letter = password[i]
        next_letter = password[i+1]

        if next_letter in letters[current_letter]:
            path += letters[current_letter][next_letter]
            if start_index == None:
                start_index = i
            current_letter = next_letter

        else:
            return None

    return path, start_index

def single_move_walks(password):
    global reverse_letters
    directions = ['n', 'e', 's', 'w', 'm', 'b', 'd', 'a']

    # take in the password and check if it is a word
    if dictionary_word(password):
        return None

    # then if not, move the first letter N and then get the new moved password and
    # check if that is a word, continue in this fashion moving in different directions
    for direction in directions:
        new_password = ''

        for i in range(len(password)):
            try:
                new_password += reverse_letters[password[i]][direction]
            except:
                break

        # don't check passwords that are not entirely letters
        if len(new_password) == len(password) and new_password.isalpha():
            if dictionary_word(new_password):
                return [direction, new_password]

    return None


def letters_flip():
    global letters
    reverse_letters = {}

    for keys, values in letters.items():
        reverse_letters[keys] = {}
        for key, value in letters[keys].items():
            reverse_letters[keys][value] = key

    return reverse_letters



if __name__ == '__main__':
    # filename = sys.argv[1]
    passwords = []

    # with open(filename, "r") as text_file:
    #     for line in text_file.read().split():
    #         passwords.append(line)

    passwords = ['qazxcv', '12345h', 'ewbr', 'otr']

    for password in passwords:
        # path, start_index = keyboard_walk(password, letters)
        # print(password, path, start_index)
        print(single_move_walks(password))
