# trie implementation testing 

import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string
import timeit 
import enchant
from nltk.corpus import wordnet as wn


d = enchant.Dict("en_US")

def dictionary_word(string):
    # here, my minimum substring length is 3 
    # returns the longest substring
    rv = False
    substrings = []
    #print(string)
    if d.check(string):
        rv = True
    for i in range(len(string)):
        for j in range(i-1,len(string)):
            substring = string[i:j]
            if j-i >= 3:
                if d.check(substring) and not substring.isdigit() :
                    rv = True
                    substrings.append(substring)
                    #print(substring)
    return rv, substrings

# extract longest dictionary word substrings from the test passwords file
list_to_check = []
with open("test_passwords.txt", "r") as file:
        for line in file:
            output = dictionary_word(line)
            if output[0]:
                output[1].sort(key = len, reverse = True)
                list_to_check.append(output[1][0])

def create_list():
    rv = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
    return rv

def create_trie_node():
    dictionary = {'count':0, 'final': False}
    return dictionary

def add_word(word,trie):
    trie['count']+= 1
    if len(word) == 0:
        trie['final'] = True
        return 
        
    # check if first character already exists
    character = word[0]
    rest_of_word = word[1:]
    
    if character in trie.keys():
        # add the rest of the word to this node
        add_word(rest_of_word,trie[character])
    else:
        # create new node
        trie[character] = create_trie_node()
        # add the rest of the word to this node
        add_word(rest_of_word,trie[character])

def is_word(word, trie):
    rv = False

    if len(word) == 0:
        return rv

    if word[0] not in trie.keys():
        return rv 
    #else:
    # base case - word with one character

    if len(word) == 1:
        if trie[word]['final'] == True:
            rv = True 
            return rv
        else:
            return rv

    # recursive call       
    if len(word)>1:
        character = word[0]
        rest_of_word = word[1:]        
        return is_word(rest_of_word,trie[character])

nouns = create_list()


def create_dictionary(master_list):
    dictionary = create_trie_node()
    for word in master_list:
        add_word(word,dictionary)
    return dictionary

dictionary = create_dictionary(nouns)


def common_nouns_list(string,nouns):
    if string in nouns:
   	    return True
    return False 


def full_list_implementation(list_of_words,nouns):
    for word in list_of_words:
        print(common_nouns_list(word,nouns))

def full_trie_implementation(list_of_words, dictionary):
    for word in list_of_words:
        print(common_nouns_trie(word,dictionary))

def common_nouns_trie(string,dictionary):
    if dictionary != None:
        if is_word(string,dictionary):
            return True
    return False 

#if __name__ == "__main__":
#    %timeit full_list_implementation(list_to_check, nouns)
#    %timeit full_trie_implementation(list_to_check,dictionary)


