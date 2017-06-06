from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol

class MRTask1(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, dictionary):
        for pattern_list in dictionary['pattern']:
            yield pattern_list[1],1

    def combiner(self,name,counts):
        sum_counts = sum(counts)
        yield name, sum_counts

    def reducer(self, name, counts):
        sum_counts = sum(counts)
        yield name, sum_counts
if __name__ == '__main__':
    MRTask1.run()
