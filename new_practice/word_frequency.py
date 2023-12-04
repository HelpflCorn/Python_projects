# Write a function that, given a string of text (possibly with punctuation and 
# line-breaks), returns an array of the top-3 most occurring words, 
# in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more 
# apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word 
# ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be 
# treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be 
# lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or 
# top-1 words should be returned, or an empty array if a text contains no words.

    
import re
from collections import Counter

def top(text):
    words = re.findall(r"[a-z']+", text.lower())
    word_counter = Counter(word for word in words if word != "'")
    most_common_words = word_counter.most_common(3)
    return [word[0] for word in most_common_words]
    
            
print(top("h'ello h'ello, go to hell"))