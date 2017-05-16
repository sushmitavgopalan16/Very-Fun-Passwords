# ':n', ':e', ':s', ':w', ':m', ':b', ':d', ':a', ':N', ':E', ':S', ':W', ':M', ':B', ':D', ':A'
# N, E, S, W, M(NE), B(NW), D(SE), A(SW)
# need to add at least shift keys that are symbols, maybe could lower letters before looking for them
# what about identical letters (ex. wwoo)
import sys

letters = {
    'q': {
        '1':'n', 'w':'e', 'a':'s', '2':'m', '`':'b', 's':'d',
        '!':'N', 'W':'E', 'A':'S', '@':'M', '~':'B', 'S':'D',
    },
    'w': {
        '2':'n', 'e':'e', 's':'s', 'q':'w', '3':'m', '1':'b', 'd':'d', 'a':'a',
        '@':'N', 'E':'E', 'S':'S', 'Q':'W', '#':'M', '!':'B', 'D':'D', 'A':'A',
    },
    'e': {
        '3':'n', 'r':'e', 'd':'s', 'w':'w', '4':'m', '2':'b', 'd':'f', 's':'a',
        '#':'N', 'R':'E', 'D':'S', 'W':'W', '$':'M', '@':'B', 'D':'F', 'S':'A',
    },
    'r': {
        '4':'n', 't':'e', 'f':'s', 'e':'w', '5':'m', '3':'b', 'g':'d', 'd':'a',
        '$':'N', 'T':'E', 'F':'S', 'E':'W', '%':'M', '#':'B', 'G':'D', 'D':'A',
    },
    't': {
        '5':'n', 'y':'e', 'g':'s', 'r':'w', '6':'m', '4':'b', 'h':'d', 'f':'a',
        '%':'N', 'Y':'E', 'G':'S', 'R':'W', '^':'M', '$':'B', 'H':'D', 'F':'A',
    },
    'y': {
        '6':'n', 'u':'e', 'h':'s', 't':'w', '7':'m', '5':'b', 'j':'d', 'g':'a',
        '^':'N', 'U':'E', 'H':'S', 'T':'W', '&':'M', '%':'B', 'J':'D', 'G':'A',
    },
    'u': {
        '7':'n', 'i':'e', 'j':'s', 'y':'w', '8':'m', '6':'b', 'k':'d', 'h':'a',
        '&':'N', 'I':'E', 'J':'S', 'Y':'W', '*':'M', '^':'B', 'K':'D', 'H':'A',
    },
    'i': {
        '8':'n', 'o':'e', 'k':'s', 'u':'w', '9':'m', '7':'b', 'l':'d', 'j':'a',
        '*':'N', 'O':'E', 'K':'S', 'U':'W', '(':'M', '&':'B', 'L':'D', 'J':'A',
    },
    'o': {
        '9':'n', 'p':'e', 'l':'s', 'i':'w', '0':'m', '8':'b', ';':'d', 'k':'a',
        '(':'N', 'P':'E', 'L':'S', 'I':'W', ')':'M', '*':'B', ':':'D', 'K':'A',
    },
    'p': {
        '0':'n', '[':'e', ';':'s', 'o':'w', '-':'m', '9':'b', "'":'d', 'l':'a',
        ')':'N', '{':'E', ':':'S', 'O':'W', '_':'M', '(':'B', '"':'D', 'L':'A',
    },
    '[': {
        '-':'n', ']':'e', "'":'s', 'p':'w', '=':'m', '0':'b', ';':'a',
        '_':'N', '}':'E', '"':'S', 'P':'W', '+':'M', ')':'B', ':':'A',
    },
    '{': {
        '-':'n', ']':'e', "'":'s', 'p':'w', '=':'m', '0':'b', ';':'a',
        '_':'N', '}':'E', '"':'S', 'P':'W', '+':'M', ')':'B', ':':'A',
    },
    ']': {
        '=':'n', '\\':'e', '[':'w', '-':'b', "'":'a',
        '+':'N', '|':'E', '{':'W', '_':'B', '"':'A',
    },
    '}': {
        '=':'n', '\\':'e', '[':'w', '-':'b', "'":'a',
        '+':'N', '|':'E', '{':'W', '_':'B', '"':'A',
    },
    '\\': {
        ']':'w', '=':'b', '}':'W', '+':'B'
    },
    '|': {
        ']':'w', '=':'b', '}':'W', '+':'B'
    },
    'a': {
        'q':'n', 's':'e', 'z':'s', 'w':'m', 'x':'d',
        'Q':'N', 'S':'E', 'Z':'S', 'W':'M', 'X':'D',
    },
    's': {
        'w':'n', 'd':'e', 'x':'s', 'a':'w', 'e':'m', 'q':'b', 'h':'c', 'f':'z',
        'W':'N', 'D':'E', 'X':'S', 'A':'W', 'E':'M', 'Q':'B', 'H':'C', 'F':'Z'
    },
    'd': {
        'e':'n', 'f':'e', 'c':'s', 's': 'w', 'r':'m', 'w':'b', 'v':'d', 'x':'a',
        'E':'N', 'F':'E', 'C':'S', 'S': 'W', 'R':'M', 'W':'B', 'V':'D', 'X':'A',
    },
    'f': {
        'r':'n', 'g':'e', 'v':'s', 'd':'w', 't':'m', 'e':'b', 'b':'d', 'c':'a',
        'R':'N', 'G':'E', 'V':'S', 'D':'W', 'T':'M', 'E':'B', 'B':'D', 'C':'A',
    },
    'g': {
        't':'n', 'h':'e', 'b':'s', 'f':'w', 'r':'m', 'y':'b', 'v':'d', 'n':'a',
        'T':'N', 'H':'E', 'B':'S', 'F':'W', 'R':'M', 'Y':'B', 'V':'D', 'N':'A',
    },
    'h': {
        'y':'n', 'j':'e', 'n':'s', 'g':'w', 't':'m', 'u':'b', 'b':'d', 'm':'a',
        'Y':'N', 'J':'E', 'N':'S', 'G':'W', 'T':'M', 'U':'B', 'B':'D', 'M':'A',
    },
    'j': {
        'u':'n', 'k':'e', 'm':'s', 'h':'w', 'y':'m', 'i':'b', 'n':'d', ',':'a',
        'U':'N', 'K':'E', 'M':'S', 'H':'W', 'Y':'M', 'I':'B', 'N':'D', '<':'A',
    },
    'k': {
        'i':'n', 'l':'e', ',':'s', 'j':'w', 'u':'m', 'o':'b', 'm':'d', '.':'a',
        'I':'N', 'L':'E', '<':'S', 'J':'W', 'U':'M', 'O':'B', 'M':'D', '>':'A',
    },
    'l': {
        'o':'n', ';':'e', '.':'s', 'k':'w', 'i':'m', 'p':'b', ',':'d', '/':'a',
        'O':'N', ':':'E', '>':'S', 'K':'W', 'I':'M', 'P':'B', '<':'D', '?':'A',
    },
    ';': {
        'p':'n', "'":'e', '/':'s', 'l':'w', 'o':'m', '[':'b', '.':'d',
        'P':'N', '"':'E', '?':'S', 'L':'W', 'O':'M', '{':'B', '>':'D',
    },
    ':': {
        'p':'n', "'":'e', '/':'s', 'l':'w', 'o':'m', '[':'b', '.':'d',
        'P':'N', '"':'E', '?':'S', 'L':'W', 'O':'M', '{':'B', '>':'D',
    },
    "'": {
        '[':'n', ';':'w', 'p':'m', ']':'b', '/':'a',
        '{':'N', ':':'W', 'P':'M', '}':'B', '?':'A',
    },
    '"': {
        '[':'n', ';':'w', 'p':'m', ']':'b', '/':'a',
        '{':'N', ':':'W', 'P':'M', '}':'B', '?':'A',
    },
    'z': {
        'a':'n', 'x':'e', 's':'b',
        'A':'N', 'X':'E', 'S':'B',
    },
    'x': {
        's':'n', 'c':'e', 'z':'w', 'd':'m', 'a':'b',
        'S':'N', 'C':'E', 'Z':'W', 'D':'M', 'A':'B',
    },
    'c': {
        'd':'n', 'v':'e', 'x':'w', 's':'m', 'f':'b',
        'D':'N', 'V':'E', 'X':'W', 'S':'M', 'F':'B',
    },
    'v': {
        'f':'n', 'b':'e', 'c':'w', 'd':'m', 'g':'b',
        'F':'N', 'B':'E', 'C':'W', 'D':'M', 'G':'B',
    },
    'b': {
        'g':'n', 'n':'e', 'v':'w', 'f':'m', 'h':'b',
        'G':'N', 'N':'E', 'V':'W', 'F':'M', 'H':'B',
    },
    'n': {
        'h':'n', 'm':'e', 'b':'w', 'g':'m', 'j':'b',
        'H':'N', 'M':'E', 'B':'W', 'G':'M', 'J':'B',
    },
    'm': {
        'j':'n', ',':'e', 'n':'w', 'h':'m', 'k':'b',
        'J':'N', '<':'E', 'N':'W', 'H':'M', 'K':'B',
    },
    ',': {
        'k':'n', '.':'e', 'm':'w', 'j':'m', 'l':'b',
        'K':'N', '>':'E', 'M':'W', 'J':'M', 'L':'B',
    },
    '<': {
        'k':'n', '.':'e', 'm':'w', 'j':'m', 'l':'b',
        'K':'N', '>':'E', 'M':'W', 'J':'M', 'L':'B',
    },
    '.': {
        'l':'n', '/':'e', ',':'w', 'k':'m', ';':'b',
        'L':'N', '?':'E', '<':'W', 'K':'M', ':':'B',
    },
    '>': {
        'l':'n', '/':'e', ',':'w', 'k':'m', ';':'b',
        'L':'N', '?':'E', '<':'W', 'K':'M', ':':'B',
    },
    '/': {
        ';':'n', '.':'w', 'l':'m', "'":'b',
        ':':'N', '>':'W', 'L':'M', '"':'B',
    },
    '?': {
        ';':'n', '.':'w', 'l':'m', "'":'b',
        ':':'N', '>':'W', 'L':'M', '"':'B',
    },
    '`': {
        '1':'e', 'q':'d',
        '!':'E', 'Q':'D',
    },
    '~': {
        '1':'e', 'q':'d',
        '!':'E', 'Q':'D',
    },
    '1': {
        '2':'e', 'q':'s', '`':'w', 'w':'d',
        '@':'E', 'Q':'S', '~':'W', 'W':'D',
    },
    '!': {
        '2':'e', 'q':'s', '`':'w', 'w':'d',
        '@':'E', 'Q':'S', '~':'W', 'W':'D',
    },
    '2': {
        '3':'e', 'e':'s', '1':'w', 'e':'d', 'q':'a',
        '#':'E', 'E':'S', '!':'W', 'E':'D', 'Q':'A',
    },
    '@': {
        '3':'e', 'e':'s', '1':'w', 'e':'d', 'q':'a',
        '#':'E', 'E':'S', '!':'W', 'E':'D', 'Q':'A',
    },
    '3': {
        '4':'e', 'e':'s', '2':'w', 'r':'d', 'w':'a',
        '$':'E', 'E':'S', '@':'W', 'R':'D', 'W':'A',
    },
    '#': {
        '4':'e', 'e':'s', '2':'w', 'r':'d', 'w':'a',
        '$':'E', 'E':'S', '@':'W', 'R':'D', 'W':'A',
    },
    '4': {
        '5':'e', 'r':'s', '3':'w', 't':'d', 'e':'a',
        '%':'E', 'R':'S', '#':'W', 'T':'D', 'E':'A',
    },
    '$': {
        '5':'e', 'r':'s', '3':'w', 't':'d', 'e':'a',
        '%':'E', 'R':'S', '#':'W', 'T':'D', 'E':'A',
    },
    '5': {
        '6':'e', 't':'s', '4':'w', 'y':'d', 'r':'a',
        '^':'E', 'T':'S', '$':'W', 'Y':'D', 'R':'A',
    },
    '%': {
        '6':'e', 't':'s', '4':'w', 'y':'d', 'r':'a',
        '^':'E', 'T':'S', '$':'W', 'Y':'D', 'R':'A',
    },
    '6': {
        '7':'e', 'y':'s', '5':'w', 'u':'d', 't':'a',
        '&':'E', 'Y':'S', '%':'W', 'U':'D', 'T':'A',
    },
    '^': {
        '7':'e', 'y':'s', '5':'w', 'u':'d', 't':'a',
        '&':'E', 'Y':'S', '%':'W', 'U':'D', 'T':'A',
    },
    '7': {
        '8':'e', 'u':'s', '6':'w', 'i':'d', 'y':'a',
        '*':'E', 'U':'S', '^':'W', 'I':'D', 'Y':'A',
    },
    '&': {
        '8':'e', 'u':'s', '6':'w', 'i':'d', 'y':'a',
        '*':'E', 'U':'S', '^':'W', 'I':'D', 'Y':'A',
    },
    '8': {
        '9':'e', 'i':'s', '7':'w', 'o':'d', 'u':'a',
        '(':'E', 'I':'S', '&':'W', 'O':'D', 'U':'A',
    },
    '*': {
        '9':'e', 'i':'s', '7':'w', 'o':'d', 'u':'a',
        '(':'E', 'I':'S', '&':'W', 'O':'D', 'U':'A',
    },
    '9': {
        '0':'e', 'o':'s', '8':'w', 'p':'d', 'i':'a',
        ')':'E', 'O':'S', '*':'W', 'P':'D', 'I':'A',
    },
    '(': {
        '0':'e', 'o':'s', '8':'w', 'p':'d', 'i':'a',
        ')':'E', 'O':'S', '*':'W', 'P':'D', 'I':'A',
    },
    '0': {
        '-':'e', 'p':'s', '9':'w', '[':'d', 'o':'a',
        '_':'E', 'P':'S', '(':'W', '{':'D', 'O':'A',
    },
    ')': {
        '-':'e', 'p':'s', '9':'w', '[':'d', 'o':'a',
        '_':'E', 'P':'S', '(':'W', '{':'D', 'O':'A',
    },
    '-': {
        '=':'e', '[':'s', '0':'w', ']':'d', 'p':'a',
        '+':'E', '{':'S', ')':'W', '}':'D', 'P':'A',
    },
    '_': {
        '=':'e', '[':'s', '0':'w', ']':'d', 'p':'a',
        '+':'E', '{':'S', ')':'W', '}':'D', 'P':'A',
    },
    '=': {
        ']':'s', '-':'w', '\\':'d', '[':'a',
        '}':'S', '_':'W', '|':'D', '{':'A',
    },
    '+': {
        ']':'s', '-':'w', '\\':'d', '[':'a',
        '}':'S', '_':'W', '|':'D', '{':'A',
    },
}

def keyboard_walk(password, letters):
    path = ''
    start_index = None
    for i in range(len(password)-1):
        current_letter = password[i]
        next_letter = password[i+1]

        if next_letter in letters[current_letter]:
            path += letters[current_letter][next_letter]
            if start_index == None:
                start_index = i
            current_letter = next_letter

        else:
            if start_index is not None:
                if len(path) < 2:
                    path = ''
                    start_index = None
                else:
                    break

    if len(path) < 2:
        path = ''
        start_index = None

    return path, start_index

if __name__ == '__main__':
    filename = sys.argv[1]
    passwords = []

    with open(filename, "r") as text_file:
        for line in text_file.read().split():
            passwords.append(line)

    for password in passwords:
        path, start_index = keyboard_walk(password, letters)
        print(password, path, start_index)
