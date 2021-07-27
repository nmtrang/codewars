"""
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
"""


def digitize(n):
    return [int(num) for num in str(n)][::-1]


print(digitize(23643235)) # [5,3,2,3,4,6,3,2]
