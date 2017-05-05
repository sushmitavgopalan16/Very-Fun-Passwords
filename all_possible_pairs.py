import sys

def all_possible_pairs(filename):
    passwords = []

    with open(filename, "r") as text_file:
        for line in text_file.read().split():
            passwords.append(line)

    password_pairs = []
    for first_pass in passwords:
        for second_pass in passwords:
            if first_pass == second_pass:
                continue
            password_pairs.append((first_pass, second_pass))

    with open(('password_pairs.txt'), "w") as output:
        output.write('\n'.join('%s %s' % pair for pair in password_pairs))

if __name__ == '__main__':
    filename = sys.argv[1]
    all_possible_pairs(filename)
