'''
Given a number, return a string with dash'-'marks before and
after each odd integer, but do not begin or end the string with
a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'

taken from https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
'''

def dashatize(num):
    if num == None:
        return "None"

    dashatized = ""
    for digit in [x for x in str(num) if x.isdigit()]:
        if int(digit) % 2 == 0:
            dashatized += digit
        else:
            if not dashatized.endswith("-") and len(dashatized) > 0:
                dashatized += "-"
            dashatized += digit + "-"

    if dashatized.endswith("-"):
        dashatized = dashatized[:-1]

    return dashatized

print(dashatize(-1234))
