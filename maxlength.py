'''
Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

https://www.codewars.com/kata/58daa7617332e59593000006/train/python
'''

def find_longest(arr):
    longest_number = min(arr) - 1
    for x in arr:
        xstr = str(x)
        if len(xstr) > len(str(longest_number)):
            longest_number = x

    return longest_number