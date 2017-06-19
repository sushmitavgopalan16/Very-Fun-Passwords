import sys
from utils.keyboard_dictionary import *
from utils.dictionary_words import dictionary_word

def keyboard_walk(password):
    '''
    Uses the letters dictionary to check if an inputted password is a keyboard walk
    Checks if the next letter in the password is in a key in any direction immediately
    around the current letter, if so, continues to check until it reaches the end of
    the string or it cannot find the next letter in the current letter's dictionary.
    If the next letter is in the current letter's dictionary, the direction needed to move
    between the current and next letter is added to the path.
    Inputs- password: string
    Outputs- path: string, start_index: int
    '''
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
    '''
    Uses the reversed letters dictionary to check if an inputted password is a
    single move walk. Each letter of the input password is moved in a specific
    direction and then the script checks whether the new collection of letters
    is a word. This is repeated for each direction.
    Inputs- password: string
    Outputs- list of direction: string, new_password: string
    '''

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
    '''
    This function flips the orientation of the letters dictionary so that it reflects
    the directons as the keys and the keys as the values
    Input- None
    Output- reverse_letters: dictionary
    '''
    global letters
    reverse_letters = {}

    for keys, values in letters.items():
        reverse_letters[keys] = {}
        for key, value in letters[keys].items():
            reverse_letters[keys][value] = key

    return reverse_letters
