"""Cuss Words are the words that make your 
language sound very impolite, rude, and culturally offensive.

``pip install better_profanity``
"""

from better_profanity import profanity
text = "Please leave me alone and just piss off. Fuck you."
censored = profanity.censor(text)
print(censored)

#it was fun