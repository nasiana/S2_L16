"""
For our practice today we are going to look at few solutions to common Python algorithms
that are frequently asked problems in coding interview rounds.

The exercises covered in this practice (together with their solutions) are adjusted interpretations of problems
available on some coding practice websites.

Solutions we present here are just indicative ones -- there might be other ways to solve tasks, but this is a god start!

MAKE SURE TO DO THIS IN XMAS HOLIDAYS
"""
####################################################################
# 1. Reverse Integer

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

## COMPLETE THE FUNCTION
def solution1(x):
    y = str(x)
    LeftIdx = 0
    RightIdx = (len(y) -1)
    z = []
    while RightIdx >= LeftIdx:
        z.append(y[RightIdx])
        RightIdx -= 1
    return ''.join(z)


print(solution1(-147))
print(solution1(852))


###################################################################
# 2. Average Words Length

# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

# come back to this

sentence1 = "Hi class, we are practicing solving algorithms. It is fun, don't you think?.."
sentence2 = "We need to work very hard to learn more about algorithms!"

import string
## COMPLETE THE FUNCTION
def solution2(sentence):
    # removes the punctuation
    return len(sentence.translate(str.maketrans('', '', string.punctuation)))

print(solution2(sentence1))
print(solution2(sentence2))


###################################################################
#3. Add strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You can use the eval() function to solve this exercise.

num1 = '257'
num2 = '2754'


## COMPLETE THE FUNCTION
def solution3(num1, num2):
    return num1 + num2


print(solution3(num1, num2))


###################################################################
# 4. First unique character

# Given an input string, find the first non-repeating character

s = 'aabccbdcbe'

## COMPLETE THE FUNCTION
def solution4(s):
    pass


print(solution4(s))

###################################################################
# 5. Monotonic Array

# Given an array of integers, determine whether the array is monotonic or not.

"""
An array is monotonic if and only if it is monotone increasing, or monotone decreasing
"""

A = [100, 6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7, 11, 22]

## COMPLETE THE FUNCTION
def solution5(nums):
    pass


print(solution5(A)) # should return True
print(solution5(B)) # should return False
print(solution5(C)) # should return True


###################################################################
# 6. Move zeros

# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

array1 = [0, 1, 0, 3, 12]  # --> should be [1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]  # --> should be [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

## COMPLETE THE FUNCTION
def solution6(nums):
    pass


solution6(array1)
solution6(array2)


###################################################################
# 7. Fill in blanks

# Given an array containing None values fill in the None values with most recent
# non None value in the array

array1 = [1, None, 2, 3, None, None, 5, None]

## COMPLETE THE FUNCTION
def solution7(array):
    pass


print(solution7(array1))


##################################################################
# 8. Matched  / Mismatched words

# Given two sentences, return an array that has the words that appear in one sentence and not
# the other and an array with the words in common.

sentence1 = 'CFG Nano has engineering and data science streams'
sentence2 = 'As part of engineering we are learning about algorithms and data structures'

## COMPLETE THE FUNCTION
def solution8(sentence1, sentence2):
    pass


print(solution8(sentence1, sentence2))


##################################################################
# 9. Prime numbers array

# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.

"""
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

interval_num = 44

## COMPLETE THE FUNCTION
def solution9(interval):
    pass


print(solution9(interval_num))