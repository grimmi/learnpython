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

    def dashit(ch):
        return "-" + ch + "-" if ch.isdigit() and int(ch) % 2 == 1 else ch

    return ''.join([dashit(x) for x in str(num)]).replace("--", "-").strip("-")

print(dashatize(-1234567))
