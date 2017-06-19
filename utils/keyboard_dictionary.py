# This file contains a dictionary giving a key on the keyboard and then the keys
# that are found in every direction relative to the key: North (N), East (E), South (S),
# West (W), Northeast (M), Northwest (B), Southeast (D), Southwest (A)

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
        '3':'n', 'r':'e', 'd':'s', 'w':'w', '4':'m', '2':'b', 'f':'d', 's':'a',
        '#':'N', 'R':'E', 'D':'S', 'W':'W', '$':'M', '@':'B', 'F':'D', 'S':'A',
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
        ']':'w', '=':'b',
        '}':'W', '+':'B'
    },
    '|': {
        ']':'w', '=':'b',
        '}':'W', '+':'B'
    },
    'a': {
        'q':'n', 's':'e', 'z':'s', 'w':'m', 'x':'d',
        'Q':'N', 'S':'E', 'Z':'S', 'W':'M', 'X':'D',
    },
    's': {
        'w':'n', 'd':'e', 'x':'s', 'a':'w', 'e':'m', 'q':'b', 'c':'d', 'z':'a',
        'W':'N', 'D':'E', 'X':'S', 'A':'W', 'E':'M', 'Q':'B', 'C':'D', 'Z':'A'
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
        't':'n', 'h':'e', 'b':'s', 'f':'w', 'y':'m', 'r':'b', 'n':'d', 'v':'a',
        'T':'N', 'H':'E', 'B':'S', 'F':'W', 'Y':'M', 'R':'B', 'N':'D', 'V':'A',
    },
    'h': {
        'y':'n', 'j':'e', 'n':'s', 'g':'w', 'u':'m', 't':'b', 'm':'d', 'b':'a',
        'Y':'N', 'J':'E', 'N':'S', 'G':'W', 'U':'M', 'T':'B', 'M':'D', 'B':'A',
    },
    'j': {
        'u':'n', 'k':'e', 'm':'s', 'h':'w', 'i':'m', 'y':'b', ',':'d', 'n':'a',
        'U':'N', 'K':'E', 'M':'S', 'H':'W', 'I':'M', 'Y':'B', '<':'D', 'N':'A',
    },
    'k': {
        'i':'n', 'l':'e', ',':'s', 'j':'w', 'o':'m', 'u':'b', '.':'d', 'm':'a',
        'I':'N', 'L':'E', '<':'S', 'J':'W', 'O':'M', 'U':'B', '>':'D', 'M':'A',
    },
    'l': {
        'o':'n', ';':'e', '.':'s', 'k':'w', 'p':'m', 'i':'b', '/':'d', ',':'a',
        'O':'N', ':':'E', '>':'S', 'K':'W', 'P':'M', 'I':'B', '?':'D', '<':'A',
    },
    ';': {
        'p':'n', "'":'e', '/':'s', 'l':'w', '[':'m', 'o':'b', '.':'a',
        'P':'N', '"':'E', '?':'S', 'L':'W', '{':'M', 'O':'B', '>':'A',
    },
    ':': {
        'p':'n', "'":'e', '/':'s', 'l':'w', '[':'m', 'o':'b', '.':'a',
        'P':'N', '"':'E', '?':'S', 'L':'W', '{':'M', 'O':'B', '>':'A',
    },
    "'": {
        '[':'n', ';':'w', ']':'m', 'p':'b', '/':'a',
        '{':'N', ':':'W', '}':'M', 'P':'B', '?':'A',
    },
    '"': {
        '[':'n', ';':'w', ']':'m', 'p':'b', '/':'a',
        '{':'N', ':':'W', '}':'M', 'P':'B', '?':'A',
    },
    'z': {
        'a':'n', 'x':'e', 's':'m',
        'A':'N', 'X':'E', 'S':'M',
    },
    'x': {
        's':'n', 'c':'e', 'z':'w', 'd':'m', 'a':'b',
        'S':'N', 'C':'E', 'Z':'W', 'D':'M', 'A':'B',
    },
    'c': {
        'd':'n', 'v':'e', 'x':'w', 'f':'m', 's':'b',
        'D':'N', 'V':'E', 'X':'W', 'F':'M', 'S':'B',
    },
    'v': {
        'f':'n', 'b':'e', 'c':'w', 'g':'m', 'd':'b',
        'F':'N', 'B':'E', 'C':'W', 'G':'M', 'D':'B',
    },
    'b': {
        'g':'n', 'n':'e', 'v':'w', 'h':'m', 'f':'b',
        'G':'N', 'N':'E', 'V':'W', 'H':'M', 'F':'B',
    },
    'n': {
        'h':'n', 'm':'e', 'b':'w', 'j':'m', 'g':'b',
        'H':'N', 'M':'E', 'B':'W', 'J':'M', 'G':'B',
    },
    'm': {
        'j':'n', ',':'e', 'n':'w', 'k':'m', 'h':'b',
        'J':'N', '<':'E', 'N':'W', 'K':'M', 'H':'B',
    },
    ',': {
        'k':'n', '.':'e', 'm':'w', 'l':'m', 'j':'b',
        'K':'N', '>':'E', 'M':'W', 'L':'M', 'J':'B',
    },
    '<': {
        'k':'n', '.':'e', 'm':'w', 'l':'m', 'j':'b',
        'K':'N', '>':'E', 'M':'W', 'L':'M', 'J':'B',
    },
    '.': {
        'l':'n', '/':'e', ',':'w', ';':'m', 'k':'b',
        'L':'N', '?':'E', '<':'W', ':':'M', 'K':'B',
    },
    '>': {
        'l':'n', '/':'e', ',':'w', ';':'m', 'k':'b',
        'L':'N', '?':'E', '<':'W', ':':'M', 'K':'B',
    },
    '/': {
        ';':'n', '.':'w', "''":'m', 'l':'b',
        ':':'N', '>':'W', '"':'M', 'L':'B',
    },
    '?': {
        ';':'n', '.':'w', "'":'m', 'l':'b',
        ':':'N', '>':'W', '"':'M', 'L':'B',
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
        '3':'e', 'w':'s', '1':'w', 'e':'d', 'q':'a',
        '#':'E', 'W':'S', '!':'W', 'E':'D', 'Q':'A',
    },
    '@': {
        '3':'e', 'w':'s', '1':'w', 'e':'d', 'q':'a',
        '#':'E', 'W':'S', '!':'W', 'E':'D', 'Q':'A',
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

reverse_letters = {
    'q': {'n': '1', 'e': 'w', 's': 'a', 'm': '2', 'b': '`', 'd': 's', 'N': '!', 'E': 'W', 'S': 'A', 'M': '@', 'B': '~', 'D': 'S'},
    'w': {'n': '2', 'e': 'e', 's': 's', 'w': 'q', 'm': '3', 'b': '1', 'd': 'd', 'a': 'a', 'N': '@', 'E': 'E', 'S': 'S', 'W': 'Q', 'M': '#', 'B': '!', 'D': 'D', 'A': 'A'},
    'e': {'n': '3', 'e': 'r', 's': 'd', 'w': 'w', 'm': '4', 'b': '2', 'd': 'f', 'a': 's', 'N': '#', 'E': 'R', 'S': 'D', 'W': 'W', 'M': '$', 'B': '@', 'D': 'F', 'A': 'S'},
    'r': {'n': '4', 'e': 't', 's': 'f', 'w': 'e', 'm': '5', 'b': '3', 'd': 'g', 'a': 'd', 'N': '$', 'E': 'T', 'S': 'F', 'W': 'E', 'M': '%', 'B': '#', 'D': 'G', 'A': 'D'},
    't': {'n': '5', 'e': 'y', 's': 'g', 'w': 'r', 'm': '6', 'b': '4', 'd': 'h', 'a': 'f', 'N': '%', 'E': 'Y', 'S': 'G', 'W': 'R', 'M': '^', 'B': '$', 'D': 'H', 'A': 'F'},
    'y': {'n': '6', 'e': 'u', 's': 'h', 'w': 't', 'm': '7', 'b': '5', 'd': 'j', 'a': 'g', 'N': '^', 'E': 'U', 'S': 'H', 'W': 'T', 'M': '&', 'B': '%', 'D': 'J', 'A': 'G'},
    'u': {'n': '7', 'e': 'i', 's': 'j', 'w': 'y', 'm': '8', 'b': '6', 'd': 'k', 'a': 'h', 'N': '&', 'E': 'I', 'S': 'J', 'W': 'Y', 'M': '*', 'B': '^', 'D': 'K', 'A': 'H'},
    'i': {'n': '8', 'e': 'o', 's': 'k', 'w': 'u', 'm': '9', 'b': '7', 'd': 'l', 'a': 'j', 'N': '*', 'E': 'O', 'S': 'K', 'W': 'U', 'M': '(', 'B': '&', 'D': 'L', 'A': 'J'},
    'o': {'n': '9', 'e': 'p', 's': 'l', 'w': 'i', 'm': '0', 'b': '8', 'd': ';', 'a': 'k', 'N': '(', 'E': 'P', 'S': 'L', 'W': 'I', 'M': ')', 'B': '*', 'D': ':', 'A': 'K'},
    'p': {'n': '0', 'e': '[', 's': ';', 'w': 'o', 'm': '-', 'b': '9', 'd': "'", 'a': 'l', 'N': ')', 'E': '{', 'S': ':', 'W': 'O', 'M': '_', 'B': '(', 'D': '"', 'A': 'L'},
    '[': {'n': '-', 'e': ']', 's': "'", 'w': 'p', 'm': '=', 'b': '0', 'a': ';', 'N': '_', 'E': '}', 'S': '"', 'W': 'P', 'M': '+', 'B': ')', 'A': ':'},
    '{': {'n': '-', 'e': ']', 's': "'", 'w': 'p', 'm': '=', 'b': '0', 'a': ';', 'N': '_', 'E': '}', 'S': '"', 'W': 'P', 'M': '+', 'B': ')', 'A': ':'},
    ']': {'n': '=', 'e': '\\', 'w': '[', 'b': '-', 'a': "'", 'N': '+', 'E': '|', 'W': '{', 'B': '_', 'A': '"'},
    '}': {'n': '=', 'e': '\\', 'w': '[', 'b': '-', 'a': "'", 'N': '+', 'E': '|', 'W': '{', 'B': '_', 'A': '"'},
    '\\': {'w': ']', 'b': '=', 'W': '}', 'B': '+'},
    '|': {'w': ']', 'b': '=', 'W': '}', 'B': '+'},
    'a': {'n': 'q', 'e': 's', 's': 'z', 'm': 'w', 'd': 'x', 'N': 'Q', 'E': 'S', 'S': 'Z', 'M': 'W', 'D': 'X'},
    's': {'n': 'w', 'e': 'd', 's': 'x', 'w': 'a', 'm': 'e', 'b': 'q', 'd': 'c', 'a': 'z', 'N': 'W', 'E': 'D', 'S': 'X', 'W': 'A', 'M': 'E', 'B': 'Q', 'D': 'C', 'A': 'Z'},
    'd': {'n': 'e', 'e': 'f', 's': 'c', 'w': 's', 'm': 'r', 'b': 'w', 'd': 'v', 'a': 'x', 'N': 'E', 'E': 'F', 'S': 'C', 'W': 'S', 'M': 'R', 'B': 'W', 'D': 'V', 'A': 'X'},
    'f': {'n': 'r', 'e': 'g', 's': 'v', 'w': 'd', 'm': 't', 'b': 'e', 'd': 'b', 'a': 'c', 'N': 'R', 'E': 'G', 'S': 'V', 'W': 'D', 'M': 'T', 'B': 'E', 'D': 'B', 'A': 'C'},
    'g': {'n': 't', 'e': 'h', 's': 'b', 'w': 'f', 'm': 'y', 'b': 'r', 'd': 'n', 'a': 'v', 'N': 'T', 'E': 'H', 'S': 'B', 'W': 'F', 'M': 'Y', 'B': 'R', 'D': 'N', 'A': 'V'},
    'h': {'n': 'y', 'e': 'j', 's': 'n', 'w': 'g', 'm': 'u', 'b': 't', 'd': 'm', 'a': 'b', 'N': 'Y', 'E': 'J', 'S': 'N', 'W': 'G', 'M': 'U', 'B': 'T', 'D': 'M', 'A': 'B'},
    'j': {'n': 'u', 'e': 'k', 's': 'm', 'w': 'h', 'm': 'i', 'b': 'y', 'd': ',', 'a': 'n', 'N': 'U', 'E': 'K', 'S': 'M', 'W': 'H', 'M': 'I', 'B': 'Y', 'D': '<', 'A': 'N'},
    'k': {'n': 'i', 'e': 'l', 's': ',', 'w': 'j', 'm': 'o', 'b': 'u', 'd': '.', 'a': 'm', 'N': 'I', 'E': 'L', 'S': '<', 'W': 'J', 'M': 'O', 'B': 'U', 'D': '>', 'A': 'M'},
    'l': {'n': 'o', 'e': ';', 's': '.', 'w': 'k', 'm': 'p', 'b': 'i', 'd': '/', 'a': ',', 'N': 'O', 'E': ':', 'S': '>', 'W': 'K', 'M': 'P', 'B': 'I', 'D': '?', 'A': '<'},
    ';': {'n': 'p', 'e': "'", 's': '/', 'w': 'l', 'm': '[', 'b': 'o', 'a': '.', 'N': 'P', 'E': '"', 'S': '?', 'W': 'L', 'M': '{', 'B': 'O', 'A': '>'},
    ':': {'n': 'p', 'e': "'", 's': '/', 'w': 'l', 'm': '[', 'b': 'o', 'a': '.', 'N': 'P', 'E': '"', 'S': '?', 'W': 'L', 'M': '{', 'B': 'O', 'A': '>'},
    "'": {'n': '[', 'w': ';', 'm': ']', 'b': 'p', 'a': '/', 'N': '{', 'W': ':', 'M': '}', 'B': 'P', 'A': '?'},
    '"': {'n': '[', 'w': ';', 'm': ']', 'b': 'p', 'a': '/', 'N': '{', 'W': ':', 'M': '}', 'B': 'P', 'A': '?'},
    'z': {'n': 'a', 'e': 'x', 'm': 's', 'N': 'A', 'E': 'X', 'M': 'S'},
    'x': {'n': 's', 'e': 'c', 'w': 'z', 'm': 'd', 'b': 'a', 'N': 'S', 'E': 'C', 'W': 'Z', 'M': 'D', 'B': 'A'},
    'c': {'n': 'd', 'e': 'v', 'w': 'x', 'm': 'f', 'b': 's', 'N': 'D', 'E': 'V', 'W': 'X', 'M': 'F', 'B': 'S'},
    'v': {'n': 'f', 'e': 'b', 'w': 'c', 'm': 'g', 'b': 'd', 'N': 'F', 'E': 'B', 'W': 'C', 'M': 'G', 'B': 'D'},
    'b': {'n': 'g', 'e': 'n', 'w': 'v', 'm': 'h', 'b': 'f', 'N': 'G', 'E': 'N', 'W': 'V', 'M': 'H', 'B': 'F'},
    'n': {'n': 'h', 'e': 'm', 'w': 'b', 'm': 'j', 'b': 'g', 'N': 'H', 'E': 'M', 'W': 'B', 'M': 'J', 'B': 'G'},
    'm': {'n': 'j', 'e': ',', 'w': 'n', 'm': 'k', 'b': 'h', 'N': 'J', 'E': '<', 'W': 'N', 'M': 'K', 'B': 'H'},
    ',': {'n': 'k', 'e': '.', 'w': 'm', 'm': 'l', 'b': 'j', 'N': 'K', 'E': '>', 'W': 'M', 'M': 'L', 'B': 'J'},
    '<': {'n': 'k', 'e': '.', 'w': 'm', 'm': 'l', 'b': 'j', 'N': 'K', 'E': '>', 'W': 'M', 'M': 'L', 'B': 'J'},
    '.': {'n': 'l', 'e': '/', 'w': ',', 'm': ';', 'b': 'k', 'N': 'L', 'E': '?', 'W': '<', 'M': ':', 'B': 'K'},
    '>': {'n': 'l', 'e': '/', 'w': ',', 'm': ';', 'b': 'k', 'N': 'L', 'E': '?', 'W': '<', 'M': ':', 'B': 'K'},
    '/': {'n': ';', 'w': '.', 'm': "''", 'b': 'l', 'N': ':', 'W': '>', 'M': '"', 'B': 'L'},
    '?': {'n': ';', 'w': '.', 'm': "'", 'b': 'l', 'N': ':', 'W': '>', 'M': '"', 'B': 'L'},
    '`': {'e': '1', 'd': 'q', 'E': '!', 'D': 'Q'}, '~': {'e': '1', 'd': 'q', 'E': '!', 'D': 'Q'},
    '1': {'e': '2', 's': 'q', 'w': '`', 'd': 'w', 'E': '@', 'S': 'Q', 'W': '~', 'D': 'W'},
    '!': {'e': '2', 's': 'q', 'w': '`', 'd': 'w', 'E': '@', 'S': 'Q', 'W': '~', 'D': 'W'},
    '2': {'e': '3', 's': 'w', 'w': '1', 'd': 'e', 'a': 'q', 'E': '#', 'S': 'W', 'W': '!', 'D': 'E', 'A': 'Q'},
    '@': {'e': '3', 's': 'w', 'w': '1', 'd': 'e', 'a': 'q', 'E': '#', 'S': 'W', 'W': '!', 'D': 'E', 'A': 'Q'},
    '3': {'e': '4', 's': 'e', 'w': '2', 'd': 'r', 'a': 'w', 'E': '$', 'S': 'E', 'W': '@', 'D': 'R', 'A': 'W'},
    '#': {'e': '4', 's': 'e', 'w': '2', 'd': 'r', 'a': 'w', 'E': '$', 'S': 'E', 'W': '@', 'D': 'R', 'A': 'W'},
    '4': {'e': '5', 's': 'r', 'w': '3', 'd': 't', 'a': 'e', 'E': '%', 'S': 'R', 'W': '#', 'D': 'T', 'A': 'E'},
    '$': {'e': '5', 's': 'r', 'w': '3', 'd': 't', 'a': 'e', 'E': '%', 'S': 'R', 'W': '#', 'D': 'T', 'A': 'E'},
    '5': {'e': '6', 's': 't', 'w': '4', 'd': 'y', 'a': 'r', 'E': '^', 'S': 'T', 'W': '$', 'D': 'Y', 'A': 'R'},
    '%': {'e': '6', 's': 't', 'w': '4', 'd': 'y', 'a': 'r', 'E': '^', 'S': 'T', 'W': '$', 'D': 'Y', 'A': 'R'},
    '6': {'e': '7', 's': 'y', 'w': '5', 'd': 'u', 'a': 't', 'E': '&', 'S': 'Y', 'W': '%', 'D': 'U', 'A': 'T'},
    '^': {'e': '7', 's': 'y', 'w': '5', 'd': 'u', 'a': 't', 'E': '&', 'S': 'Y', 'W': '%', 'D': 'U', 'A': 'T'},
    '7': {'e': '8', 's': 'u', 'w': '6', 'd': 'i', 'a': 'y', 'E': '*', 'S': 'U', 'W': '^', 'D': 'I', 'A': 'Y'},
    '&': {'e': '8', 's': 'u', 'w': '6', 'd': 'i', 'a': 'y', 'E': '*', 'S': 'U', 'W': '^', 'D': 'I', 'A': 'Y'},
    '8': {'e': '9', 's': 'i', 'w': '7', 'd': 'o', 'a': 'u', 'E': '(', 'S': 'I', 'W': '&', 'D': 'O', 'A': 'U'},
    '*': {'e': '9', 's': 'i', 'w': '7', 'd': 'o', 'a': 'u', 'E': '(', 'S': 'I', 'W': '&', 'D': 'O', 'A': 'U'},
    '9': {'e': '0', 's': 'o', 'w': '8', 'd': 'p', 'a': 'i', 'E': ')', 'S': 'O', 'W': '*', 'D': 'P', 'A': 'I'},
    '(': {'e': '0', 's': 'o', 'w': '8', 'd': 'p', 'a': 'i', 'E': ')', 'S': 'O', 'W': '*', 'D': 'P', 'A': 'I'},
    '0': {'e': '-', 's': 'p', 'w': '9', 'd': '[', 'a': 'o', 'E': '_', 'S': 'P', 'W': '(', 'D': '{', 'A': 'O'},
    ')': {'e': '-', 's': 'p', 'w': '9', 'd': '[', 'a': 'o', 'E': '_', 'S': 'P', 'W': '(', 'D': '{', 'A': 'O'},
    '-': {'e': '=', 's': '[', 'w': '0', 'd': ']', 'a': 'p', 'E': '+', 'S': '{', 'W': ')', 'D': '}', 'A': 'P'},
    '_': {'e': '=', 's': '[', 'w': '0', 'd': ']', 'a': 'p', 'E': '+', 'S': '{', 'W': ')', 'D': '}', 'A': 'P'},
    '=': {'s': ']', 'w': '-', 'd': '\\', 'a': '[', 'S': '}', 'W': '_', 'D': '|', 'A': '{'},
    '+': {'s': ']', 'w': '-', 'd': '\\', 'a': '[', 'S': '}', 'W': '_', 'D': '|', 'A': '{'},
}