import datetime 
from dateutil.parser import parse

def find_date(num_string):
	date_fmts = ('%Y%m%d', '%Y%d%m', '%m%d%Y', '%d%m%Y','%Y%m','%m%Y', '%Y') 
	is_date = False
	for format in date_fmts:
		try:
			test = datetime.datetime.strptime(num_string, format)
			print("HOORAY IS DATE")
			print(test)
			is_date = True
			break
		except ValueError:
			print(num_string, "NOT DATE")

	return is_date

'''
1 million false positives- any numbers can be turned into dates :(

def find_date2(num_string):
	try:
		test = parse(num_string)
		print("HOORAY IS DATE")
		print(test)
	except ValueError:
		print(num_string, "NOT DATE")


'''




if __name__ == "__main__":
	is_date = find_date('2013')
	print(is_date)
