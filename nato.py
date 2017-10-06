'''
The idea for this Kata came from 9gag today.here

You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.

Like this:

Input: If you can read

Output: India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta

Some notes

    Keep the punctuation, and remove the spaces.
    Use Xray without dash or space.

Reference

alt text

You can use the NATO hash with the alphabet

taken from: https://www.codewars.com/kata/586538146b56991861000293/train/python
'''
NATO = {"A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot",
        "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima",
        "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
        "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "Xray",
        "Y": "Yankee", "Z": "Zulu"}

def to_nato(words):
    return ' '.join([NATO[c.upper()] if c.isalpha() else c for c in ''.join(words.split())])

print(to_nato("if you can read"))
