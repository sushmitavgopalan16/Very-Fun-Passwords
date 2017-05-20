import datetime 
import find_subsequence

def find_date(num_string):
	date_fmts = ('%Y%m%d', '%Y%d%m', '%m%d%Y', '%d%m%Y','%Y%m','%m%Y', '%Y', '%m%d', '%d%m') 
	is_date = False
	for format in date_fmts:
		try:
			date = datetime.datetime.strptime(num_string, format)
			if date.year > 1700 and date.year < 2017:
				is_date = True
				break
		except ValueError:
			continue
	if is_date:
		return date
	else:
		return None


def find_sequence(num_string):
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
		return "Sequence"
	elif rep:
		return "Repitition"
	else:
		return None


def classify_num_string(num_string):
	sequence_type = find_sequence(num_string)
	if sequence_type:
		return (sequence_type, num_string)
	else:
		date = find_date(num_string)
		if date:
			return ("Date", num_string)
		else:
			return("Nothing", num_string)


















