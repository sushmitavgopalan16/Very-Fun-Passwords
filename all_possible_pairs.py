import sys

def all_possible_pairs(filename):

    with open(('password_pairs.txt'), "w") as output:
        with open(filename, "r") as first_file:
            i1 = 0
            for first in first_file:
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
    all_possible_pairs(filename)