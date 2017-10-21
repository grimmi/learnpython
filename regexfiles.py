'''
Are you a file extension master?
Let's find out by checking if Bill's files are images or audio files.
Please use regex if available natively for your language.

You will create 2 string methods:

isAudio/is_audio,
matching 1 or + uppercase/lowercase letter(s) (combination possible),
with the extension .mp3, .flac, .alac, or .aac.

isImage/is_image,
matching 1 or + uppercase/lowercase letter(s) (combination possible),
with the extension .jpg, .jpeg, .png, .bmp, or .gif.

Note that this is not a generic image/audio files checker.
It's meant to be a test for Bill's files only. 
Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only

Rules

It should return true or false, simply.
File extensions should consist of lowercase letters and numbers only.
File names should consist of letters only (uppercase, lowercase, or both)
Good luck!

taken from: https://www.codewars.com/kata/574bd867d277832448000adf/train/python
'''

import re

def is_audio(filename):
    pattern = re.compile("^([\w\d]+).(mp3|flac|alac|aac)$", re.IGNORECASE)
    
    return True if pattern.match(filename) else False

print(is_audio("NothingElseMatters.mp3"))
