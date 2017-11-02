'''
Build Tower

Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ', 
  '    ***    ', 
  '   *****   ', 
  '  *******  ', 
  ' ********* ', 
  '***********'
]

taken from https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python
'''

def tower_builder(n_floors):

    max_width = n_floors * 2 - 1

    def make_floor(n):
        floor_width = 2 * n - 1
        padding_width = int((max_width - floor_width) / 2)
        padding = ' ' * padding_width
        return padding + '*' * floor_width + padding
    
    return [make_floor(x + 1) for x in range(0, n_floors)]

print(tower_builder(6))