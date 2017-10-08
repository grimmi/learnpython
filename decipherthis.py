'''
Decipher this!
You are given several secret messages you need to decipher. Here are the conditions:

The first letter corresponds to ASCII character code (case sensitive)
The second letter needs to be switched to the last letter
The last letter needs to be switched to the second letter
If it only has one letter, it will be unchanged
If it only has two letters, you will just need to convert the ASCII character code to a letter
Keepin' it simple -- there are no special characters

Example:
decipherThis('72olle 103doo 100ya'); // 'Hello good day'
decipherThis('82yade 115te 103o'); // 'Ready set go'

taken from: https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python
'''

def decipher_this(word):
    ascii_code = ""
    for c in word:
        if not c.isdigit(): 
            break
        ascii_code += c

    first_letter = chr(int(ascii_code))

    return first_letter

print(decipher_this("82"))