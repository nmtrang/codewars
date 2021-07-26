"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers 
differs from the others. Bob observed that one number usually differs from the others in evenness. 
Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

**** Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples:
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd
"""

def iq_test(numbers):
    noOfOdd = 0
    noOfEven = 0

    numbers = numbers.split(' ')
    for number in numbers:
        if int(number) % 2 == 0:
            noOfEven += 1
        else:
            noOfOdd += 1

    if noOfEven > noOfOdd:
        for i in range(0, len(numbers)):
            if int(numbers[i]) % 2 != 0:
                return numbers.index(numbers[i]) + 1
    else:
        for i in range(0, len(numbers)):
            if int(numbers[i]) % 2 == 0:
                return numbers.index(numbers[i]) + 1


"""
AFTER REFACTORING
def iq_test(numbers):
    even_odd_check = [int(i) % 2 for i in numbers.split(' ')]

    if even_odd_check.count(0) > 1:
        return even_odd_check.index(1) + 1
    else:
        return even_odd_check.index(0) + 1
"""

print(iq_test('2 3 7 5 11'))  # 1
