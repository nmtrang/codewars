"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    return [i for i in seq if seq.count(i) % 2 != 0][0]


print(find_it([5,4,3,2,1,5,4,3,2,10,10]))  # 1
