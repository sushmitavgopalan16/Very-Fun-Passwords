import sys

def all_possible_pairs(filename):

    with open(('password_pairs.txt'), "w") as output:
        with open(filename, "r") as first_file:
            for first in first_file:
                with open(filename, "r") as second_file:
                    for second in second_file:
                        first = first.strip()
                        second = second.strip()
                        pair = first + ' ' + second + '\n'
                        output.write(pair)

if __name__ == '__main__':
    filename = sys.argv[1]
    all_possible_pairs(filename)
