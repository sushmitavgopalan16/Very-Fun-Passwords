from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol

	def mapper(self, _, dictionary):
		pattern = dictionary['pattern']
		all_patterns = []

		for single_pat in pattern:
			all_patterns.append(single_pat[1])

		yield all_patterns, 1


	def reducer(self, pattern, count):
		counts = sum(count)

		yield pattern, counts


if __name__ == '__main__':
	MRPasswords.run()
