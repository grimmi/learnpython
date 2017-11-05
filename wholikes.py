'''
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. We want to create the text that should be displayed
next to such an item.

Implement a function likes :: [String] -> String, which must take in input array,
containing the names of people who like an item. It must return the display text
as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For more than 4 names, the number in and 2 others simply increases.

taken from: https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
'''

def likes(names):
    nl = len(names)
    if nl == 0:
        return "no one likes this"
    elif nl == 1:
        return "{} likes this".format(names[0])
    elif nl == 2:
        return "{} and {} like this".format(*names)
    elif nl == 3:
        return "{}, {} and {} like this".format(*names)
    else:
        return "{}, {} and {n} others like this".format(*names, n=nl-2)

print(likes(["hans", "max", "franz", "andi"]))