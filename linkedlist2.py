'''
Linked Lists - Length & Count

Implement Length() to count the number of nodes in a linked list.

length(null) === 0
length(1 -> 2 -> 3 -> null) === 3

Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) === 0
count(1 -> 2 -> 3 -> null, 1) === 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) === 4

I've decided to bundle these two functions within the same Kata since they are both very similar.

The push()/Push() and buildOneTwoThree()/BuildOneTwoThree() functions do not need to be redefined.

taken from: http://www.codewars.com/kata/linked-lists-length-and-count/train/python
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    return 0 if node is None else 1 + length(node.next)

def count(node, data):
    if node is None:
        return 0
    if node.data == data:
        return 1 + count(node.next, data) if not node.next is None else 1
    else:
        return 0 + count(node.next, data) if not node.next is None else 0