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

from math import sqrt

def count_even_digits(n):
    return sum((str(n).count(x) for x in ['0', '2', '4', '6', '8']))

def is_prime(n):
    if n in [2, 3, 5, 7, 11, 13, 17, 19]:
        return True
    if n < 23:
        return False
    upper_limit = int(sqrt(n))

    for candidate in range(2, upper_limit):
        if n % candidate == 0:
            return False

    return True

def f(n):
    max_prime = 2
    max_even_count = 1
    for x in range(23, n):
        if is_prime(x):
            digitcount = count_even_digits(x)
            if x > max_prime and digitcount >= max_even_count:
                max_even_count = digitcount
                max_prime = x
    return max_prime

print(f(10000))