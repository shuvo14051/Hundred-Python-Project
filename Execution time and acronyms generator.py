"""
The execution or running time 
of the program indicates how 
quickly the output is delivered based on 
the algorithm you used to solve the problem. 
"""

from time import time
start =  time()

# Python program to create acronyms
word = input("Enter any word:")
li = word.split()
a = ""
for item in li:
    a = a + (item[0].upper())
print(a)

end = time()
execution_time = end-start
print(execution_time)