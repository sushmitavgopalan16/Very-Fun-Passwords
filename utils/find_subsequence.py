def check_similars(substring, password):
	for i, char in enumerate(substring):
		# print(char, password[i])
		if char != password[i]:
			# print("RETURNING FAAAAAAALSE")
			return False

	return True


def get_start_index(substring, password):
	if len(substring) == 0:
		return
	for i, char in enumerate(password):
		#print(i, char)
		if char == substring[0]:
			# print("THINGS ARE THE SAME")
			if(check_similars(substring[1:], password[i+1:])):
				return i

	return None

def check_alpha(substring):
	is_alpha = None
	if substring.isalpha():
		is_alpha = True
	elif substring.isdigit():
		is_alpha = False

	return is_alpha


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

	if len(substring) > 2:
		start_index1 = get_start_index(substring, l_pass1)
		start_index2 = get_start_index(substring, l_pass2)

		is_alpha = check_alpha(substring)

		return [substring, is_alpha, [[l_pass1, start_index1], [l_pass2, start_index2]]]
	else:
		return None


if __name__ == "__main__":
	thing = substring('123testing', '123test')
	print(thing)
