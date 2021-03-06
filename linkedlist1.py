'''
Linked Lists - Push & BuildOneTwoThree

Write push() and buildOneTwoThree() functions to easily update and
initialize linked lists. Try to use the push() function within your
buildOneTwoThree() function.

Here's an example of push() usage:

var chained = null
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null

The push function accepts head and data parameters, where head is either
a node object or null/None/nil. Your push implementation should be able
to create a new linked list/node when head is null/None/nil.

The buildOneTwoThree function should create and return a linked list with three nodes:
1 -> 2 -> 3 -> null

taken from: http://www.codewars.com/kata/linked-lists-push-and-buildonetwothree/train/python
'''

class Node(object):
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

def push(head, data):
    return Node(data, head)

def build_one_two_three():
    return push(push(push(None, 3), 2), 1)

chain = push(None, 1)
chain = push(chain, 2)
chain = push(chain, 3)

print(chain)