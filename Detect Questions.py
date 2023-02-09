"""
Detecting questions means identifying whether 
a sentence is interrogative or not. 
"""

from nltk.tokenize import word_tokenize
question_words = ["what", "why", "when", "where", 
             "name", "is", "how", "do", "does", 
             "which", "are", "could", "would", 
             "should", "has", "have", "whom", "whose", "don't"]

question = input("Enter a sentence:").lower()
token = word_tokenize(question)

first_word = token[0]
if first_word in question_words:
    print("This is a question!")
else:
    print("This is not a question!")

