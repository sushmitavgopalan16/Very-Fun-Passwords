# Go over list of passwords and generate a boolean that is True
# if some substring of >= 3 characters of the password is a dictionary word\
# trie implementation testing
import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string
import timeit
from python-nltk.corpus import wordnet as wn

def create_trie_node():
    dictionary = {'count':0, 'final': False}
    return dictionary

def add_word(word,trie):
	trie['count']+= 1
	if len(word) == 0:
		trie['final'] = True
		return

	character = word[0]
	rest_of_word = word[1:]

	if character in trie.keys():
		add_word(rest_of_word,trie[character])
	else:
		# create new node
		trie[character] = create_trie_node()
		# add the rest of the word to this node
		add_word(rest_of_word,trie[character])

def is_word(word, trie):
	rv = False
	# base case length = 0
	if len(word) == 0:
		return rv

	if word[0] not in trie.keys():
		return rv

	if len(word) == 1:
		if trie[word]['final']:
			rv = True
			return rv
		else:
			return rv

	# recursive call
	if len(word)>1:
		character = word[0]
		rest_of_word = word[1:]
		return is_word(rest_of_word,trie[character])

def build_dictionary(word_list):
	dictionary = create_trie_node()
	for word in word_list:
		add_word(word,dictionary)
	return dictionary

def build_dictionary_from_file(filename):
	dictionary = create_trie_node()
	with open(filename, "r") as file:
		for line in file:
			add_word((line.split()[0].lower()),dictionary)
	return dictionary

# build dictionaries

#COMMON NOUNS
list_common_nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}
common_nouns = build_dictionary(list_common_nouns)

# ALL DICTIONARY WORDS
list_all_words = {x.name().split('.', 1)[0] for x in wn.all_synsets()}
all_words = build_dictionary(list_all_words)

# LAST NAMES
last_names_dict = build_dictionary_from_file("text_files/last_names.txt")
#
# FEMALE NAMES
female_names_dict = build_dictionary_from_file("text_files/female_first_names.txt")

# MALE NAMES
male_names_dict = build_dictionary_from_file("text_files/male_first_names.txt")

def dictionary_word(word):
	global all_words
	return is_word(word,all_words)

def common_noun(word):
	global common_nouns
	return is_word(word,common_nouns)

def last_names(word):
	global last_names_dict
	return is_word(word,last_names_dict)
#
def female_names(word):
	global female_names_dict
	return is_word(word,female_names_dict)

def male_names(word):
	global male_names_dict
	return is_word(word,male_names_dict)
