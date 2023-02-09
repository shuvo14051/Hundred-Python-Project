"""SequenceMatcher is a class in Python available 
in the difflib module,mwhich provides functions for 
comparing sequences in two different pieces of text.
"""
from difflib import SequenceMatcher

text1 = "Younus Ahamed Shuvo".lower()
text2 = "Israt Jahan Urmi".lower()

sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100:.2f}% similar.")