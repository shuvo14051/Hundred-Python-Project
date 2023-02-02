"""
Given an array containing a range of 
numbers from 0 to n with a missing number, 
find the missing number in the input array.
"""
def findMissingNum(n):
    numbers = set(n)
    output = []
    for i in range(n[0], n[-1]):
        if i not in numbers:
            output.append(i)
    return output

li = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(findMissingNum(li))