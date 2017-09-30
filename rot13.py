'''
ROT13 is a simple letter substitution cipher that replaces
a letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string
ciphered with Rot13. If there are numbers or special characters
included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using "encode" in Python is considered cheating.

taken from https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
'''

def rotate(char):
    if not char.isalpha():
        return char
    diff = 65 if char.istitle() else 97
    return chr((((ord(char) - diff) + 13) % 26) + diff)

def rot13(message):
    return ''.join(map(rotate, message))

print(rot13("abcdefghijklmnopqrstuvwxyz"))
print(rot13("m"))
