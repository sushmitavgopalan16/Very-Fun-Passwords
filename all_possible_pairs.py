import sys

def all_possible_pairs(filename):
    passwords = []

    with open(filename, "r") as text_file:
        for line in text_file.read().split():
            passwords.append(line)

            with open(('password_pairs.txt'), "w") as output:
                for i in range(len(passwords)):
                    for j in range(i+1,len(passwords)):
                        pair = passwords[i] + ' ' + passwords[j] + '\n'
                        output.write(pair)

if __name__ == '__main__':
    filename = sys.argv[1]
    all_possible_pairs(filename)
