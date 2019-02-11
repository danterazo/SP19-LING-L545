# LING-L 445: Practical 1B
# Dante Razo, drazo
# Code provided by Francis M. Tyers

import sys

counter = 0

for c in sys.stdin.read():
    if c in 'аэиоу':
        counter += 1
print(counter)
