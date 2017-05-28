from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from find_subsequence import substring
from keyboard_walks import keyboard_walk, single_move_walks
from num_patterns import classify_num_string
from nltk.corpus import wordnet as wn
from dictionary_words import dictionary_word
from dictionary_words import common_noun
from dictionary_words import last_names
from dictionary_words import female_names
from dictionary_words import male_names
from mrjob.protocol import JSONValueProtocol

WORD_RE = re.compile(r"[\w]+")

class MRPairSubstrings(MRJob):

	OUTPUT_PROTOCOL = JSONValueProtocol

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
			if result:
				sub_dict['word'] = result

			# check if common noun
			if result:
				commonnoun = common_noun(sub[0])
				if commonnoun:
					sub_dict['common_noun'] = commonnoun

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

		if sub[1] is False or sub[1] is None:
			num_result = classify_num_string(sub[0])
			if num_result:
				sub_dict[num_result[0]] = num_result[1]
		yield sub[0], sub_dict

	def mapper_single_move_walks(self, sub, sub_dict):
		walk = single_move_walks(sub)
		if walk:
			print(walk, walk[0], walk[1])
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
