'''
A string is considered to be in title case if each word in the
string is either (a) capitalised (that is, only the first letter
of the word is in upper case) or (b) considered to be an exception
and put entirely into lower case unless it is the first word,
which is always capitalised.

Write a function that will convert a string into title case, given
an optional list of exceptions (minor words). The list of minor
words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string
-- it should behave in the same way even if the case of the minor
word string is changed.

###Arguments (Haskell)

    First argument: space-delimited list of minor words that must
    always be lowercase except for the first word in the string.
    Second argument: the original string to be converted.

###Arguments (Other languages)

    First argument (required): the original string to be converted.
    Second argument (optional): space-delimited list of minor words
    that must always be lowercase except for the first word in the string.
    The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.

###Example

title_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 'The Wind in the Willows'
title_case('the quick brown fox') # should return: 'The Quick Brown Fox'


taken from: https://www.codewars.com/kata/5202ef17a402dd033c000009/train/python
'''

def title_case(title, minor_words = None):

    if title is None or title == '':
        return ''

    lower_minors = [] if minor_words is None else [w.lower() for w in minor_words.split(' ')]
    sentence = title.split(' ')
    title_cased = [sentence[0].capitalize()]
    for word in sentence[1:]:
        if word.lower() in lower_minors:
            title_cased.append(word.lower())
        else:
            title_cased.append(word.capitalize())
    
    return ' '.join(title_cased)

print(title_case("a clash of KINGS", "a an the of"))