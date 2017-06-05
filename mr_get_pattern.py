from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol


	def mapper(self, _, dictionary):
		pattern = dictionary['pattern']

		yield pattern[0][1], 1


	def reducer(self, pattern, count):
		counts = sum(count)

		yield pattern, counts


if __name__ == '__main__':
	MRPasswords.run()
