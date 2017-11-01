'''
A stream of data is received and needs to be reversed.
Each segment is 8 bits meaning the order of these segments need to be reversed:

11111111 00000000 00001111 10101010

(byte1) (byte2) (byte3) (byte4)

10101010 00001111 00000000 11111111

(byte4) (byte3) (byte2) (byte1)

Total number of bits will always be a multiple of 8.
The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]

taken from: https://www.codewars.com/kata/569d488d61b812a0f7000015/train/python
'''

def data_reverse(data):

    def chunk(ns, size):
        for x in range(0, len(ns), size):
            yield ns[x:x + size]

    chunks = reversed(list(chunk(data, 8)))
    return sum(chunks, [])

print(data_reverse([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]))
