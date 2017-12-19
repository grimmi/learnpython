'''
Find the closest prime number under a certain integer n that has the maximum possible amount of even digits.

For n = 1000, the highest prime under 1000 is 887, having two even digits (8 twice)

Naming f(), the function that gives that prime, the above case and others will be like the following below.

f(1000) ---> 887 (even digits: 8, 8)

f(1210) ---> 1201 (even digits: 2, 0)

f(10000) ---> 8887

f(500) ---> 487

f(487) ---> 467

taken from https://www.codewars.com/kata/582dcda401f9ccb4f0000025/train/python
'''

def count_even_digits(n):
    return sum((str(n).count(x) for x in ['0', '2', '4', '6', '8']))

print(count_even_digits(24))