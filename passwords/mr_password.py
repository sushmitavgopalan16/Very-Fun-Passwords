from mrjob.job import MRJob
from mrjob.step import MRStep
from mrjob.protocol import JSONValueProtocol
from utils.find_patterns import find_patterns

class MRPasswords(MRJob):

	INPUT_PROTOCOL = JSONValueProtocol
	OUTPUT_PROTOCOL = JSONValueProtocol

	def mapper_on_passwords(self, _, dictionary):
		'''
		Mapper- takes in dictionary produced by mr_substring, creates new
		dictionary based on password
		Inputs- dictionary: dictionary from mr_substring 
		Outputs- password[0]: the name of the password that we're reducing on 
				 tuple of subsequence information:
				 	-At index[0] you find the name of the subsequence 
				 	-At index[1] you find the starting index of the subsequence 
				 	in relation to the password
				 	-At index[3] you find the 'flag' of the subsequence which 
				 	tells you if the subsequence is a word/name/number sequence etc. 
		'''
		passwords = set()

		for password in dictionary['passwords']:
			if 'male_name' in dictionary:
				flag = 'male name'
			elif 'female_name' in dictionary:
				flag = 'female name'
			elif 'word' in dictionary:
				flag = 'word'
			elif 'last_name' in dictionary:
				flag = 'last name'
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
		'''
		Reducer- Reduces on the name of the password 
		Inputs- password: Name of the password
				sub: substring information as described above
		Outputs- password: Name of the password
				 subsequences: list of subsequences and relevant information that
				 pertain to that password 

		'''
		subsequences = list(sub)
		yield password, subsequences

	def mapper_get_patterns(self, password, sub):		
		'''
		Mapper #2- Finds and yields specific pattern for each password 
		Inputs- password: name of the password
				sub: list of subsequences and information contained within each
				specific password 
		Outputs- pass_dict: a dictionary containing the password and the pattern
				 discovered within the password 
		'''
		pattern = find_patterns(password, sub)

		if len(pattern) > 0:
			pass_dict = {'password':password, 'pattern': pattern}

			yield None, pass_dict


	def steps(self):
		return [
			MRStep(mapper=self.mapper_on_passwords,
				reducer=self.reducer_on_passwords),
			MRStep(mapper=self.mapper_get_patterns)]


if __name__ == '__main__':
	MRPasswords.run()
