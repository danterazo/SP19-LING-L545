# LING-L 445: Practical 02
# Dante Razo, drazo, 2/11/19
# Code provided by Francis M. Tyers

import sys

a = 0  # This is a variable for counting the number of vowels

for c in sys.stdin.read():
    print('Main loop:', a, c, file=sys.stderr)
    if c in 'аэиоуяеыёю':
        print('Found a vowel!', c, file=sys.stderr)
        a = a + 1

print(a)
