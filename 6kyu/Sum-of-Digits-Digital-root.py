"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

# RECURSIVE FUNCTION ALWAYS COME TO MY MIND


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))
    # return the sum if < 10
    # else recursively sum the digits when n < 10 is met


print(digital_root(9)) # 9
print(digital_root(10)) # 1
print(digital_root(493193)) # 2


"""
AMAZING SOLUTION OF OTHER (so much respect to this guy!!!)
VERY CLEVER SOLUTION (but not a best practice!)
def digital_root(n):
    return n % 9 or n and 9
"""


