"""
Problem Statement​ ​1:
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
"""

wordlist = ["This", "is", "a", "beautiful", "day"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))
