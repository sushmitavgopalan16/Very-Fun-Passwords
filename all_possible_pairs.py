import sys

def all_possible_pairs(filename):
    passwords = []

    with open(filename, "r") as text_file:
        for line in text_file.read().split():
            passwords.append(line)

    password_pairs = []
    for i in range(len(passwords)):
        for j in range(i+1,len(passwords)):
            password_pairs.append((passwords[i], passwords[j]))

    with open(('password_pairs.txt'), "w") as output:
        output.write('\n'.join('%s %s' % pair for pair in password_pairs))

if __name__ == '__main__':
    filename = sys.argv[1]
    all_possible_pairs(filename)
