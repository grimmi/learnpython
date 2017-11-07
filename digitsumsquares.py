'''
The number 81 has a special property, a certain power of the
sum of its digits is equal to 81 (nine squared). Eighty one (81),
is the first number in having this property (not considering numbers of one digit).
The next one, is 512. Let's see both cases with the details

8 + 1 = 9 and 92 = 81

512 = 5 + 1 + 2 = 8 and 83 = 512

We need to make a function, power_sumDigTerm(), that receives a number n and may
output the n-th term of this sequence of numbers. The cases we presented above means that

power_sumDigTerm(1) == 81

power_sumDigTerm(2) == 512

Happy coding!
'''

def power_sumDigTerm(n):

    def sum_of_digits(x):
        return sum([int(c) for c in str(x)])

    def is_some_power_of(x, max):
        if x == 1:
            return False

        print("is %d some power of %d?" % (x, max))
        power = 2
        powered = pow(x, power)
        while(powered < max):
            power = power + 1
            powered = pow(x, power)

        return powered == max

    def infinite():
        i = 2
        while 1:
            yield i
            i += 1
    
    found = 0
    for i in infinite():
        print("checking %d..." % i)
        digitsum = sum_of_digits(i)
        print("digitsum: %d" % digitsum)
        if(is_some_power_of(digitsum, i)):
            found = found + 1
        if found == n:
            return i

    return -1

print(power_sumDigTerm(2))