from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w]+")

class MRPairDistances(MRJob):

    def mapper(self, _, line):
        for pair in line.split('\n'):
            first, second = pair.split()
            distance = levenshtein(first, second)
            yield (first, second), distance

    def reducer(self, pair, distances):
        for distance in distances:
            if distance < 5:
                yield pair, distance

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper
def memoize(func):
    mem = {}
    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]
    return memoizer
@call_counter
@memoize
def levenshtein(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t)+1,
               levenshtein(s, t[:-1])+1,
               levenshtein(s[:-1], t[:-1]) + cost])
    return res

if __name__ == '__main__':
    MRPairDistances.run()
