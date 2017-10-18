'''
Description:

Each exclamation mark weight is 2; Each question mark weight is 3.
Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is
more heavy, return "Right"; If they are balanced, return "Balance".

Examples

balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
'''

def balance(left, right):

    def sum_side(side):
        return sum([2 if c == '!' else 3 for c in side])

    left_sum = sum_side(left)
    right_sum = sum_side(right)

    return "Left" if left_sum > right_sum else "Right" if right_sum > left_sum else "Balance"

print(balance("!!", "??"))