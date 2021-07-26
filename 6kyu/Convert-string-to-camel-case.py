"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    list = [c for c in text]

    for c in range(len(list)):
        if list[c] in ('_', '-'):  # hello_world
            list[c + 1] = list[c + 1].upper()  # hello_World

    return ''.join([c for c in list if c not in ('_', '-')])


print(to_camel_case('hello_world_My_name_is_Cheng'))
