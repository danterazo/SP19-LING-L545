# LING-L 445: Practical 1B
# Dante Razo, drazo
# This program imitates the Unix 'cat' command

import sys

# Read in everything from standard input
text = sys.stdin.read()  # NOTE: unintelligble output; unicode issue

# Output everything to standard output
sys.stdout.write(text)
