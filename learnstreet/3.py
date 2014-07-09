#ROT-13 Project
from string import ascii_uppercase, ascii_lowercase
import math
import string
def string_rot13():
    # ROT-13 is a simple substitution cypher. It stands for
    # "ROTate by 13 places." The cypher replaces any letter
    # (a-z or A-Z) with the one that appears 13 sequential places
    # behind it. Note that for the last half of the alphabet, the
    # ROT-13 character loops back around to the beginning of the
    # alphabet. Also note that characters that aren't in the alphabet
    # are passed through.
    "Return a string in its ROT-13 format"
    ss = raw_input('please input something-->:   ')
    total = []
    out = ''
    lower = string.ascii_lowercase*2
    upper = string.ascii_uppercase*2
    "REPLACE THIS CODE WITH ROT-13 METHOD"
    for letter in ss:
        if letter in lower:
            input = ord(letter)
            output = lower[input+13-97]
            out += output
        else :
            input = ord(letter)
            output = lower[input+13-65]
            out += output
    print out
    return out
    
def main():
    string_rot13()
    for chr in str:
        if chr in ascii_uppercase:
            index = (ascii_uppercase.find(chr) + 13) % 26
            total.append(ascii_uppercase[index])
        elif chr in ascii_lowercase:
            index = (ascii_lowercase.find(chr) + 13) % 26
            total.append(ascii_lowercase[index])
        else:
            total.append(chr)
    return ''.join(total)

if __name__== "__main__":
    main()