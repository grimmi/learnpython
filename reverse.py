'''
Complete the solution so that it reverses the string value passed into it.

solution('world') # returns 'dlrow'
'''

def solution(string):
    rev = ""
    for char in string:
        rev = char + rev
    return rev

print(solution("hallo"))
