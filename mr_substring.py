from mrjob.job import MRJob
from mrjob.step import MRStep
import re
from find_subsequence import substring
from keyboard_walks import keyboard_walk
from dictionary_words import dictionary_word

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
    	if sub[1] == True or sub[1] == None:
	        result = dictionary_word(sub[0])
	        sub_dict['word'] = result
        if sub[1] == False of sub[1] == None:
        	# must add call to number functions, find year, num sequence etc. 
        	num_result = sub[0]
        	sub_dict['number'] = num_result
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
