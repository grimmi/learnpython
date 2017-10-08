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

def decipher_this(words):
    def decipher_word(word):
        ascii_code = ""
        for c in word:
            if not c.isdigit(): 
                break
            ascii_code += c

        first_letter = chr(int(ascii_code))
        word = word.replace(ascii_code, "", 1)
        new_word = first_letter

        if len(word) == 0:
            return new_word
        
        if len(word) == 1:
            return new_word + word[-1]
        else:
            new_word += word[-1]
            new_word += word[1:-1]
            new_word += word[0]
            return new_word

    return ' '.join(decipher_word(word) for word in words.split(' '))

print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))