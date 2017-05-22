from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from find_subsequence import substring
from keyboard_walks import keyboard_walk
from num_patterns import classify_num_string
from nltk.corpus import wordnet as wn
from dictionary_words import dictionary_word
from dictionary_words import common_noun
from dictionary_words import last_names
from dictionary_words import female_names
from dictionary_words import male_names

WORD_RE = re.compile(r"[\w]+")

class MRPairSubstrings(MRJob):

	def mapper_find_substrings(self, _, line):
		for pair in line.split('\n'):
			first, second = pair.split()
			result = substring(first, second)
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
			sub_dict['word'] = result

			# check if common noun
			if sub_dict['word']:
				commonnoun = common_noun(sub[0])
				sub_dict['common_noun'] = commonnoun

		# check if last name
		if sub[1] is False or sub[1] is None:
			lastname = last_names(sub[0])
			sub_dict['last_name'] = lastname

		# check if female name
		if sub[1] is False or sub[1] is None:
			femalename = female_names(sub[0])
			sub_dict['female_name'] = femalename

		# check if male name
		if sub[1] is False or sub[1] is None:
			malename = male_names(sub[0])
			sub_dict['male_name'] = malename



		if sub[1] is False:
			# must add call to number functions, find year, num sequence etc.
			num_result = classify_num_string(sub[0])
			if num_result:
				sub_dict[num_result[0]] = num_result[1]
		yield sub[0], sub_dict

	def mapper_walks(self, sub, sub_dict):
		path = keyboard_walk(sub)
		sub_dict['walks'] = path
		yield sub, sub_dict

	def steps(self):
		return [
		  MRStep(mapper=self.mapper_find_substrings,
				reducer=self.reducer_find_substrings),
		  MRStep(mapper=self.mapper_find_words),
		  MRStep(mapper=self.mapper_walks)]

if __name__ == '__main__':
	MRPairSubstrings.run()
