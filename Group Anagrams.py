from collections import defaultdict

"""
Anagrams are words formed by rearranging the letters of another word, 
For example, car and arc, cat and act, etc. 
Grouping anagrams is one of the popular questions in coding interviews.
"""
def group_anagram(a):
    # passing the list class
    # so that we can append values
    d = defaultdict(list)
    for i in a:
        # sorted(i) with return a list like ['a','e','t']
        # "".join will convert it into a single string
        # that will be used as the key of the dictionary
        sorted_i = "".join(sorted(i))
        d[sorted_i].append(i)
    for i in d.values():
        print(i)
  

words = ["tea", "eat", "bat", "ate", "arc", "car"]
group_anagram(words)  
