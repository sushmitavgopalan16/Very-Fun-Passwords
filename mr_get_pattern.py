from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol

	def mapper(self, _, dictionary):
		'''
		Mapper- reading in dictionary from mr_password and creating counts 
				of specific patterns 
		Inputs- dictionary: dictionary of password information from mr_password
		Outputs- all_patterns: pattern found in individual pattern 
		'''
		pattern = dictionary['pattern']
		all_patterns = []

		for single_pat in pattern:
			all_patterns.append(single_pat[1])

		yield all_patterns, 1


	def reducer(self, pattern, count):
		'''
		Reducer- reduce on patterns, getting the final count of each pattern 
		'''
		counts = sum(count)

		yield pattern, counts


if __name__ == '__main__':
	MRPasswords.run()
