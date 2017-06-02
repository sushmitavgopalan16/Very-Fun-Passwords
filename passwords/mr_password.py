from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from utils.find_patterns import find_patterns

class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol

	def mapper_on_passwords(self, _, dictionary):
		for password in dictionary['passwords']:
			if 'common_noun' in dictionary:
				flag = 'proper noun'		
			elif 'female_name' in dictionary:
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
			else:
				flag = None

			yield password[0], (dictionary['subsequence'], password[1], flag)

	def reducer_on_passwords(self, password, sub):
		subsequences = list(sub)
		yield None, (password, subsequences)

	def mapper_get_patterns(self, _, pass_subs):
		pattern = find_patterns(pass_subs[0], pass_subs[1])

		all_patterns = []
		for pat in pattern:
			all_patterns.append(pat[1])

		yield all_patterns, 1


	def reducer_on_patterns(self, pattern, count):
		# reduce on None, keep the pattern and counts
		counts = sum(count)
		patterns = list(pattern)

		yield None, (patterns, counts)




	def steps(self):
		return [
		  MRStep(mapper=self.mapper_on_passwords,
				reducer=self.reducer_on_passwords),
		  MRStep(mapper=self.mapper_get_patterns, 
		  		reducer=self.reducer_on_patterns)]



if __name__ == '__main__':
	MRPasswords.run()



	# MRStep(mapper=self.mapper_get_patterns,
		  		# reducver=self.reducer_on_patterns)