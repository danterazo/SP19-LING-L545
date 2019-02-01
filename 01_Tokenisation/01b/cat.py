"""
This is my program that acts like
the Unix 'cat' command
"""
import sys

# Read in everything from standard input
text = sys.stdin.read()

# Output everything to standard output
#sys.stdout.write(text) #TODO: unicode output
print(text)
