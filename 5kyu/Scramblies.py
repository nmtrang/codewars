"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters 
can be rearranged to match str2, otherwise returns false.

Notes:
Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
from collections import Counter


def scramble(s1, s2):
    count = Counter(s1) 
    count.subtract(Counter(s2))
    return (all(i >= 0 for i in count.values()))


print(scramble('cedewaraaossoqqyt', 'codewars'))  # True
print(scramble('katas', 'steak'))  # False
