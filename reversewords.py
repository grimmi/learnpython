'''
Write a reverseWords function that accepts a string a
parameter, and reverses each word in the string.
Every space should stay, so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpmaxe"

reverseWords "An example!"    -- "nA !elpmaxe"
reverseWords "double  spaces" -- "elbuod  secaps"


taken from https://www.codewars.com/kata/reverse-words
'''

def reverse_words(string):
    return ' '.join(map(lambda w: ''.join(w[::-1]), string.split(' ')))

print(reverse_words("hallo! welt"))