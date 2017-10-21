'''
The main idea is to count all the occuring characters(UTF-8) in string.
If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }

taken from https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
'''

#method with used taken from here: https://stackoverflow.com/a/37163210/1344058
def count(word):
    used = set()
    return dict([(c, word.count(c)) for c in word if c not in used and (used.add(c) or True)])

print(count("hallo"))