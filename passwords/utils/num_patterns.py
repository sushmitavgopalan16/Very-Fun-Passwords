import datetime

def find_date(num_string):
	'''
	Determines whether string of numbers and/or words is a date using 
	datetime objects 
	'''
	date_fmts = ('%Y%m%d', '%Y/%m/%d', '%Y%d%m', '%Y/%d/%m', '%m%d%Y','%m/%d/%Y', '%d%m%Y', '%d/%m/%Y', '%Y%m','%m%Y', '%Y', '%m%d', '%d%m', '%d%b%Y', '%d%B%Y', '%b%d%Y', '%B%d%Y', '%d%B', '%d%b', '%b%d', '%B%d')
	is_date = False
	for i, format in enumerate(date_fmts):
		try:
			date = datetime.datetime.strptime(num_string, format)
			# if the month is spelled out, consider it a date, regardless of year
			if '%b' in format:
				is_date = True
				break
			# if the date is just numbers, only include it if it's between 1700
			#  and 2017 
			elif date.year > 1700 and date.year < 2017:
				is_date = True
				break
		except ValueError:
			continue
	if is_date:
		return date
	else:
		return None


def find_sequence(num_string):
	'''
	Checks if there is a sequence or repition in a string of numbers 
	'''
	str_len = len(num_string) -1
	str_dif = 0
	prev_num = int(num_string[0])
	seq = True
	rep = True
	for i,num in enumerate(num_string):
		if i > 0:
			str_dif = int(num)-int(prev_num)
			if abs(str_dif) == 1:
				prev_num = int(num)
				rep = False
			elif str_dif == 0:
				seq = False
			else:
				seq = False
				rep = False
				break

	if seq:
		return "sequence"
	elif rep:
		return "repitition"
	else:
		return None


def classify_num_string(num_string):
	'''
	Using sequence and date functions to classify string of numbers as date, 
	repition, sequence, or nothing
	'''
	if num_string.isdigit():
		sequence_type = find_sequence(num_string)
		if sequence_type:
			return (sequence_type, num_string)
		else:
			date = find_date(num_string)
			if date:
				return ("date", num_string)
			else:
				return ("numbers", num_string)
	else:
		date = find_date(num_string)
		if date:
			return ("date", num_string)
		else:
			return None
