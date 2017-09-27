'''
Find the number with the most digits.

If two numbers in the argument array have the same number of digits,
return the first one in the array.

https://www.codewars.com/kata/58daa7617332e59593000006/train/python
'''
def find_longest(arr):
    return max(arr, key=lambda x: len(str(x)))

print(find_longest([123, 345, 56666]))
