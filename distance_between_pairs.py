from mrjob.job import MRJob
import re
from find_subsequence import substring

WORD_RE = re.compile(r"[\w]+")

class MRPairDistances(MRJob):

    def mapper(self, _, line):
        for pair in line.split('\n'):
            first, second = pair.split()
            result = substring(first, second)
            if result is not None:
                sub = result[0]
                pass1 = result[1][0]
                pass2 = result[1][1]
                # print(type(pass1), pass1)
                yield sub, pass1
                yield sub, pass2

    def reducer(self, sub, pairs):
        make_list = list(pairs)
        #flat_list = []
        #for sublist in make_list:
        #    for item in sublist:
        #        flat_list.append(item)
        print(make_list)
        #unique_list = list(set(flat_list))
        yield sub, make_list


if __name__ == '__main__':
    MRPairDistances.run()
