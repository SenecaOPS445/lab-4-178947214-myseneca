#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    """
    Returns the first five characters of the given string.
    :param s: Input string.
    :return: First five characters of the input string.
    """
    return s[:5]

def last_seven(s):
    """
    Returns the last seven characters of the given string.
    :param s: Input string.
    :return: Last seven characters of the input string.
    """
    return s[-7:]

def middle_number(num):
    """
    Returns the second and third characters of the given number converted to a string.
    :param num: Input number (integer or float).
    :return: String containing the second and third characters.
    """
    num_str = str(num)
    if len(num_str) > 2:
        return num_str[1:3]
    return ''

def first_three_last_three(s1, s2):
    """
    Returns a string that starts with the first three characters of s1 and ends with the last three characters of s2.
    :param s1: First input string.
    :param s2: Second input string.
    :return: Combined string as described.
    """
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))             # Output: Hello
    print(first_five(str2))             # Output: Senec
    print(last_seven(str1))             # Output: World!!
    print(last_seven(str2))             # Output: College
    print(middle_number(num1))          # Output: 50
    print(middle_number(num2))          # Output: .5
    print(first_three_last_three(str1, str2))  # Output: HelCollege
    print(first_three_last_three(str2, str1))  # Output: SenWorld!!

