# Morse code, converts to written and spoken

# needed to run the speak command on apple computers
import os

# morse code dict from stackoverflow
code = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

# spoken dictionary conversion
spoken_code = {}

# fill the spoken_code dict with values
for key, item in code.items():
    new_item = item.replace('.', 'dot ')
    new_item = new_item.replace('-', 'dash ')
    spoken_code[key] = new_item

# ask for user input
input_str = input('Type a string to convert to morse code: ')

# upper the string so it will be found in the dict
input_str = input_str.upper()

# speak each letter and print it to the terminal
for letter in input_str:
    if letter != ' ':
        print(f'{letter} {code[letter]}')
        os.system(f'say {spoken_code[letter]}')
    else:
        print(' ')
