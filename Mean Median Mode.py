# Mean
li = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
li.sort()
mean = sum(li)/len(li)
print("Mean" ,mean)

# Median
length = len(li)
if (length%2 == 0):
    m1 = li[length//2]
    m2 = li[length//2 - 1]
    median = (m1+m2)/2
else:
    median = li[length//2]

print("Median",median)

# Mode

d = {}
for i in li:
    if i in d:
        d[i]+=1
    else:
        d[i] = 1
"""
maximum = max(d.values())
for key, value in d.items():
    if value==maximum:
        mode = key
print(mode)
"""

"""
It's possible to implement line 27 to 31 in 
a single line using a list comprehension
"""
mode = [key for key, value in d.items() if value == max(d.values())]
print("Mode", mode[0])
