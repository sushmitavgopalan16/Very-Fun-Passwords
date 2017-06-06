import os
import sys
from sys import exit
import tty
import termios
import fcntl
import string
import timeit

def create_trie_node():
	'''
	Creates a node with count initialized to 1
	and 'final' initialized to False
	'''
	dictionary = {'count':0, 'final': False}
	return dictionary

def add_word(word,trie):
	'''
	Takes a word and a trie and
	adds the word recursively to the trie
	'''
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
	'''
	Takes a word and a trie and returns True if the word
	exists in the given trie and False, otherwise.
	'''
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
	'''
	Returns a large trie containing all the words
	in the a given list
	'''
	dictionary = create_trie_node()
	for word in word_list:
		add_word(word,dictionary)
	return dictionary

def build_dictionary_from_file(filename):
	'''
	Returns a large trie containing all the words
	from the fist column in a given text file
	'''
	dictionary = create_trie_node()
	with open(filename, "r") as file:
		for line in file:
			word = line.split()[0].lower()
			if len(word) >3:
				add_word(word,dictionary)
	return dictionary

# build dictionaries

# 10k most popular DICTIONARY WORDS
#list_all_words = {x.name().split('.', 1)[0] for x in wn.all_synsets()}
#all_words = build_dictionary(list_all_words)
all_words = build_dictionary_from_file("./text_files/10k_words.txt")

# LAST NAMES
last_names_dict = build_dictionary_from_file("./text_files/last_names.txt")
#
# FEMALE NAMES
female_names_dict = build_dictionary_from_file("./text_files/female_first_names.txt")

# MALE NAMES
male_names_dict = build_dictionary_from_file("./text_files/male_first_names.txt")

def dictionary_word(word):
	'''
	returns True if the word belongs to our dictionary
	of dictionary words and False, otherwise
	'''
	global all_words
	return is_word(word,all_words)

def last_names(word):
	'''
	returns True if the word belongs to our dictionary
	of last names and False, otherwise
	'''
	global last_names_dict
	return is_word(word,last_names_dict)

def female_names(word):
	'''
	returns True if the word belongs to our dictionary
	of female names and False, otherwise
	'''
	global female_names_dict
	return is_word(word,female_names_dict)

def male_names(word):
	'''
	returns True if the word belongs to our dictionary
	of male names and False, otherwise
	'''
	global male_names_dict
	return is_word(word,male_names_dict)
