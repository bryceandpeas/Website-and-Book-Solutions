'''

Codewars Kata - 8 Kyu - They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?

Description:

They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it series #1:
Are they opposite?

Task

Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.
The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string

Some examples:

isOpposite("ab","AB") should return true;
isOpposite("aB","Ab") should return true;
isOpposite("aBcd","AbCD") should return true;
isOpposite("AB","Ab") should return false;
isOpposite("","") should return false;

'''

def is_opposite(s1,s2):
    if s1 == '' and s2 == '':
        return False
    else:
        return True if s1.swapcase() == s2 else False