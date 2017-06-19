import string

def is_punct(subsequence):
	'''
	Iterate through a password and determine whether it is all punctuation.
	Input- subsequence: string
	Output- punct: bool indicating whether all punctuation or not
	'''
	punct = True
	for char in subsequence:
		if char not in string.punctuation:
			punct = False

	return punct
