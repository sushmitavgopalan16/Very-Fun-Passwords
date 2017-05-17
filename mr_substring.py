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
                sub = result[0]
                pass1 = result[1][0]
                pass2 = result[1][1]
                yield sub, pass1
                yield sub, pass2

    def reducer_find_substrings(self, sub, pairs):
        sub_dict = {"passwords": list(pairs)}
        print(sub, sub_dict)
        yield sub, sub_dict

    def mapper_find_words(self, sub, passwords):
        result = dictionary_word(sub)

        # if result is not None:


    def mapper_walks(self, sub, passwords):
        for password in passwords:
            path = keyboard_walk(password[0])
            if path is not None:
                yield (sub, password[0]), path

    def steps(self):
        return [
          MRStep(mapper=self.mapper_find_substrings,
                 reducer=self.reducer_find_substrings),
          MRStep(mapper=self.mapper_find_words),
          MRStep(mapper=self.mapper_walks)]

if __name__ == '__main__':
    MRPairSubstrings.run()
