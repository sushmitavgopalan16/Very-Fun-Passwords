from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from find_patterns import find_patterns


class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol
	OUTPUT_PROTOCOL = JSONValueProtocol

	def mapper_on_passwords(self, _, dictionary):
		for password in dictionary['passwords']:	
			if 'female_name' in dictionary:
				flag = 'female name'
			elif 'male_name' in dictionary:
				flag = 'male name'
			elif 'last_name' in dictionary:
				flag = 'last name'
			elif 'word' in dictionary:
				flag = 'word'
			elif 'sequence' in dictionary:
				flag = 'sequence'
			elif 'date' in dictionary:
				flag = 'date'
			elif 'repitition' in dictionary:
				flag = 'repitition'
			elif 'walks' in dictionary:
				flag = 'keyboard walk'
			else:
				flag = None

		yield password, (dictionary['subsequence'], password[1], flag)

	def reducer_on_passwords(self, password, sub):
		new_dict = {}
		subsequences = list(sub)

		new_dict['subsequences'] = []
		new_dict['subsequences'].append(subsequences[0])

		new_dict['password'] = password

		yield password, new_dict

	def mapper_get_patterns(self, password, dictionary):
		test =find_patterns(dictionary['password'][0], dictionary['subsequences'])

		dictionary['pattern'] = test
		yield None, dictionary


	def steps(self):
		return [
		  MRStep(mapper=self.mapper_on_passwords,
				reducer=self.reducer_on_passwords),
		  MRStep(mapper=self.mapper_get_patterns)]



if __name__ == '__main__':
	MRPasswords.run()