import pdb

def find_patterns(password, subs):
	# password = name of password
	# sub = tuple(name, starting index, flag)
	#print("\n\nin find patterns file!\n")
	parse_string = True
	substrings = sorted(subs, key=lambda x: x[1])

	#print(substrings)

	end_i = 0
	starting_sub = None
	limit = -1
	pattern = []

	#print("password is", password)
	#print("subsequences are", subs)
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
			#print("appending pattern")
			limit = end_i
			pattern.append((keep_sub[0], keep_sub[2]))

	#
	# print("pattern is", pattern)
	return pattern


if __name__ == "__main__":
	null = None
	subs = [["789", 3, "sequence"]]
	passw = "********"

	thing = find_patterns(passw, subs)
	print(thing)