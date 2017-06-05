

def find_patterns(password, subs):
	'''
	Finds the patterns of subsequence types in each password 
	Inputs- password: name of the password 
			subs: list of subsequences included in the password 
			along with relevant information about each subsequence
				-at index[0] you find the name of the subsequence 
				-at index[1] you find the starting index of the subsequence 
				in the password
				-at index[2] you find the flag of that subsequence 
	Outputs- pattern: a list of tuples.
				-at index[0] you find the name of the subsequence 
				-at index[1] you find the flag of that subsequence 
	'''
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
			if sub[1] is not None:
				if sub[1] > limit and sub[1] <= start_i and (sub[1] + len(sub[0])-1) > end_i:
					#print('things are good!')
					if sub[2]:
						start_i = sub[1]
						end_i = sub[1] + len(sub[0]) -1 
						keep_sub = sub
						parse_string = True

		if parse_string:
			# avoiding duplicate entries
			limit = end_i
			pattern.append((keep_sub[0], keep_sub[2]))


	return pattern

