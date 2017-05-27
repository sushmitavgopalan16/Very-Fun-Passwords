

def find_patterns(password, subs):
	# password object = dictionary- has list of subsequences 
	# sub = tuple(name, starting index, flag)
	parse_string = True
	substrings = sorted(subs, key=lambda x: x[1])

	end_i = 0
	starting_sub = None
	limit = -1
	pattern = []

	# goes through each subsequence and gets the best pattern
	while parse_string:
		parse_string = False
		start_i = len(password) -1
		for sub in substrings:		
			if sub[1] > limit and sub[1] <= start_i and sub[1] + len(sub[0]) > end_i:
				start_i = sub[1]
				end_i = sub[1] + len(sub[0])
				keep_sub = sub
				parse_string = True

		if parse_string:
			# avoiding duplicate entries 
			limit = end_i
			pattern.append((keep_sub[0], keep_sub[2]))

	return pattern





