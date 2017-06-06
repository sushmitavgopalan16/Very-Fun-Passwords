from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from utils.find_patterns import find_patterns

class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol
	OUTPUT_PROTOCOL = JSONValueProtocol

	def mapper_on_passwords(self, _, dictionary):
		passwords = set()

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
			elif 'numbers' in dictionary:
				flag = 'numbers'
			elif 'walks' in dictionary:
				flag = 'keyboard walk'
			elif 'single_move_walks' in dictionary:
				flag = 'single move w'
			elif 'punctuation' in dictionary:
				flag = 'punctuation'
			else:
				flag = None

			passwords.add((password[0], password[1]))

		for password in passwords:
			yield password[0], (dictionary['subsequence'], password[1], flag)

	def reducer_on_passwords(self, password, sub):
		subsequences = list(sub)
		print(password, subsequences)
		yield password, subsequences

	def mapper_get_patterns(self, password, sub):

		pattern = find_patterns(password, sub)

		if pattern:
			pass_dict = {'password':password, 'pattern': pattern}

			yield None, pass_dict


	def steps(self):
		return [
			MRStep(mapper=self.mapper_on_passwords,
				reducer=self.reducer_on_passwords),
			MRStep(mapper=self.mapper_get_patterns)]


if __name__ == '__main__':
	MRPasswords.run()
