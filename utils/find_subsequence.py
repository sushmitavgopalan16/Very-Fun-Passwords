def check_similars(substring, password):
	for i, char in enumerate(substring):
		if char != password[i]:
			return False

	return True


def get_start_index(substring, password):
	if len(substring) == 0:
		return
	for i, char in enumerate(password):
		if char == substring[0]:
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
