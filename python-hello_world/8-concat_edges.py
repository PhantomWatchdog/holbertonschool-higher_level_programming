#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split()
display = [words[i] for i in [5, 6, 12, 0]]
print(' '.join(display))
