import sys
import threading
import itertools

def all_possible_pairs(filename, start, end):
	'''
	Opens 2 copies of passwords file and creates all possible pairs 
	Inputs- filename: name of file
			start: index where specific thread should begin in file
			end: index where specific thread should end in file 
	'''
	output_file = 'password_pairs_{}.txt'.format(ID)
	with open((output_file), "w") as output:
		with open(filename, "r") as first_file:
			i1 = start
			for first in itertools.islice(first_file, start, end):
				with open(filename, "r") as second_file:
					i2 = 0
					for second in second_file:
						first = first.strip()
						second = second.strip()
						if i2 > i1:
							pair = first + ' ' + second + '\n'
							output.write(pair)
						i2 += 1
				i1 += 1

if __name__ == '__main__':
	filename = sys.argv[1]
	num_threads = int(sys.argv[2])

	# splitting file into equal-ish parts for threading 
	num_lines = sum(1 for line in open(filename))
	remainder=num_lines%num_threads
	integer = num_lines/num_threads

	splits=[]
	for i in range(num_threads):
		splits.append(integer)
	for i in range(remainder):
		splits[i]+=1

	start = 0 
	threads = []

	#creating and running pairs function in multiple threads 
	for i, num in enumerate(splits):
		if i != 0:
			start = int(end) 
		end = int(start + num)

		t = threading.Thread(target=all_possible_pairs, args = (filename, start, end))
		threads.append(t)
		t.start()

