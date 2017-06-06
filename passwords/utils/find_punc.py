import string

def is_punct(subsequence):
	punct = True
	for char in subsequence:
		if char not in string.punctuation:
			punct = False

	return punct
