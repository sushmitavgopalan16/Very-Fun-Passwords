import sys

def all_possible_pairs(filename):
    '''
    Creates a new file that contains all possible pairs of the inputted passwords.
    Does not create duplicates, such as: password1, password2 and password2, password1
    i1 and i2 can be altered to shorten the list of input passwords that are used to
    create the passwords. Change them to be the number of passwords you would like,
    such as 100.
    Inputs- filename: string
    Outputs- password_pairs.txt: file
    '''

    with open(('password_pairs.txt'), "w") as output:
        with open(filename, "r") as first_file:
            i1 = 0
            for first in first_file:
                with open(filename, "r") as second_file:
                    i2 = 0
                    for second in second_file:
                        first = first.strip()
                        second = second.strip()
                        if i2 > 100:
                            break
                        if i2 > i1:
                            pair = first + ' ' + second + '\n'
                            output.write(pair)
                        i2 += 1

                i1 += 1
                if i1 >= 100:
                    break

if __name__ == '__main__':
    filename = sys.argv[1]
    all_possible_pairs(filename)
