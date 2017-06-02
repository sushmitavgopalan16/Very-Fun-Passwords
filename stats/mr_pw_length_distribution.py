from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol

# note - this gets the distribution for the PASSWORDS, not subsequences
class MRTaskLengthDistribution(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, _, dictionary):
        for password in dictionary['passwords']:
            # throw away actual password
            yield str(len(password[0])),1
            #yield len(password[0]),1

    def combiner(self,name,counts):
        sum_counts = sum(counts)
        yield name, sum_counts

    def reducer(self, name, counts):
        sum_counts = sum(counts)
        yield name, sum_counts


if __name__ == '__main__':
    MRTaskLengthDistribution.run()
