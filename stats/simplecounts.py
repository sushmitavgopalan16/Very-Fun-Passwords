from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol

class MRTaskSimpleCounts(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, dictionary):
        if 'common_noun' in dictionary:
            yield 'common_noun',1

        if 'female_name' in dictionary:
            yield 'common_noun',1

        if 'male_name' in dictionary:
            yield 'common_noun',1

        if 'last_name' in dictionary:
            yield 'common_noun',1

        if 'word' in dictionary:
            yield 'word',1

        if 'sequence' in dictionary:
            yield 'sequence',1

        if 'date' in dictionary:
            yield 'date',1

        if 'repitition' in dictionary:
            yield 'repitition',1

        if 'numbers' in dictionary:
            yield 'numbers',1

        if 'walks' in dictionary:
            yield 'walks',1

        if 'single_move_walks' in dictionary:
            yield 'single_move_walks',1


    def combiner(self,name,counts):
        sum_counts = sum(counts)
        yield name, sum_counts

    def reducer(self, name, counts):
        sum_counts = sum(counts)
        yield name, sum_counts


if __name__ == '__main__':
    MRTaskSimpleCounts.run()
