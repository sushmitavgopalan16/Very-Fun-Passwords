# Go over list of passwords and generate a boolean that is True
# if some substring of >= 3 characters of the password is a dictionary word
import enchant
d = enchant.Dict("en_US")

def dictionary_word(string):
    # here, my minimum substring length is 3
    rv = False
    print(string)
    if d.check(string):
        rv = True
    for i in range(len(string)):
        for j in range(i-1,len(string)):
            substring = string[i:j]
            if j-i >= 3:
                if d.check(substring):
                    rv = True
                    print(substring)
                    break;
    return rv

if __name__ == "__main__":
    s = "gehasfsdfsstuffzzzzz"
    print(str(dictionary_word(s)))
