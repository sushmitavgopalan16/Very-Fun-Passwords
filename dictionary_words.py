# Go over list of passwords and generate a boolean that is True
# if some substring of >= 3 characters of the password is a dictionary word\
import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string
from find_subsequence import get_start_index, check_similars

from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}

import enchant
d = enchant.Dict("en_US")
from nltk.tag import pos_tag


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
    
    sub_indices = []

    for sub in substrings:
    	start_i = get_start_index(sub, string)
    	sub_indices.append([sub, start_i])

    return rv, sub_indices

def common_nouns(string):
   if string in nouns:
   	return True
   return False 


# trie implementation testing 

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

dictionary = create_trie_node()
for word in nouns:
	add_word(word,dictionary)


if __name__ == "__main__":
	with open("test_passwords.txt", "r") as file:
		for line in file:
			output = dictionary_word(line)
			if output[0]:
				print(line, output[1])
			'''
			if output[0]:
				print(str(is_word(output[1][0],dictionary)))
			'''
