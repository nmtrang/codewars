"""
Write an algorithm that takes an array and moves all of the zeros 
to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(array):
    current = 0
    for i in array:
        if i != 0:
            array[current] = i
            current += 1

    for i in range(current, len(array)):
        array[i] = 0

    return array   


print(move_zeros([1, 0, 0, 2, 5, 7, 0, 10]))
