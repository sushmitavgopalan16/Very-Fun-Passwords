

def subsequence(pass1, pass2):
	#get lowercase for analysis 
	l_pass1 = pass1.lower()
	l_pass2 = pass2.lower()

	#creates list of size(pass1) full of lists of size(pass2)
	lengths = [[0 for j in range(len(l_pass2)+1)] for i in range(len(l_pass1)+1)]

    # row 0 and column 0 are initialized to 0 already
	for i, x in enumerate(l_pass1):
		for j, y in enumerate(l_pass2):
			if x == y:
				lengths[i+1][j+1] = lengths[i][j] + 1
			else:
				lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
	# read the substring out from the matrix
	subseq = ""
	x, y = len(l_pass1), len(l_pass2)
	while x != 0 and y != 0:
		if lengths[x][y] == lengths[x-1][y]:
			x -= 1
		elif lengths[x][y] == lengths[x][y-1]:
			y -= 1
		else:
			assert l_pass1[x-1] == l_pass2[y-1]
			subseq = l_pass1[x-1] + subseq
			x -= 1
			y -= 1


	return subseq


def substring(pass1, pass2):
	l_pass1 = pass1.lower()
	l_pass2 = pass2.lower()

	m = [[0] * (1 + len(l_pass2)) for i in range(1 + len(l_pass1))]
	longest, x_longest = 0, 0
	for x in range(1, 1 + len(l_pass1)):
		for y in range(1, 1 + len(l_pass2)):
			if l_pass1[x - 1] == l_pass2[y - 1]:
				m[x][y] = m[x - 1][y - 1] + 1
				if m[x][y] > longest:
					longest = m[x][y]
					x_longest = x
			else:
				m[x][y] = 0

	substring = l_pass1[x_longest - longest: x_longest]

	return substring


if __name__ == "__main__":
	s1 = "coolio"
	s2 = "cool4io"
	name1 = subsequence(s1, s2)
	name2 = substring(s1, s2)

	s1_prop1 = len(name1)/len(s1)
	s1_prop2 = len(name2)/len(s1)

	s2_prop1 = len(name1)/len(s2)
	s2_prop2 = len(name2)/len(s2)


	print("subsequence is", name2)
	print("\n", s1, "subsequence proprtion", s1_prop2)
	print("\n", s2, "subsequence proprtion", s2_prop2)




