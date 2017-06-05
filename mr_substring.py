#!/usr/bin/env python3
import re
import sys
from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol

from utils.find_subsequence import substring
from utils.keyboard_walks import keyboard_walk, single_move_walks
from utils.num_patterns import classify_num_string
from utils.find_punc import is_punct
from utils.dictionary_words import dictionary_word
from utils.dictionary_words import last_names
from utils.dictionary_words import female_names
from utils.dictionary_words import male_names

WORD_RE = re.compile(r"[\w]+")

class MRPairSubstrings(MRJob):

	OUTPUT_PROTOCOL = JSONValueProtocol

	def mapper_find_substrings(self, _, line):
		for pair in line.split('\n'):
			try:
				first, second = pair.split()
			except:
				print('[PAIR ERROR]', pair, file=sys.stderr)
				continue

			try:
				result = substring(first, second)
			except:
				print('[PAIR ERROR]', pair, file=sys.stderr)
				continue

			if result is not None:
				sub = (result[0], result[1])
				pass1 = result[2][0]
				pass2 = result[2][1]
				yield sub, pass1
				yield sub, pass2

	def reducer_find_substrings(self, sub, pairs):
		sub_dict = {"passwords": list(pairs)}
		yield sub, sub_dict

	def mapper_find_words(self, sub, sub_dict):

		# check if dictionary word
		if sub[1] is True or sub[1] is None:
			result = dictionary_word(sub[0])
			if result:
				sub_dict['word'] = result

		# check if last name

			lastname = last_names(sub[0])
			if lastname:
				sub_dict['last_name'] = lastname

		# check if female name

			femalename = female_names(sub[0])
			if femalename:
				sub_dict['female_name'] = femalename

		# check if male name

			malename = male_names(sub[0])
			if malename:
				sub_dict['male_name'] = malename

		# throw it to the number script
		if sub[1] is False or sub[1] is None:
			num_result = classify_num_string(sub[0])
			if num_result:
				sub_dict[num_result[0]] = num_result[1]

		# throw it to the punctuation script
		if sub[1] is None:
			if is_punct(sub[0]):
				sub_dict['punctuation'] = sub[0]

		yield sub[0], sub_dict

	def mapper_single_move_walks(self, sub, sub_dict):
		walk = single_move_walks(sub)
		if walk:
			sub_dict['single_move_walks'] = [walk[0], walk[1]]
		yield sub, sub_dict

	def mapper_walks(self, sub, sub_dict):
		path = keyboard_walk(sub)
		if path:
			sub_dict['walks'] = path

		sub_dict['subsequence'] = sub

		yield None, sub_dict

	def steps(self):
		return [
		  MRStep(mapper=self.mapper_find_substrings,
				reducer=self.reducer_find_substrings),
		  MRStep(mapper=self.mapper_find_words),
		  MRStep(mapper=self.mapper_single_move_walks),
		  MRStep(mapper=self.mapper_walks)]

if __name__ == '__main__':
	MRPairSubstrings.run()
