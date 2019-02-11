# LING-L 445: Practical 1B
# Dante Razo, drazo
import sys


def wc():
    # returns (line count, word count, character count
    lc, wc, cc, sc = 0, 0, 0, 0

    # counting; space delimiter for words
    for c in sys.stdin.read():
        cc += 1

        if c is '\n':
            lc += 1
        elif c is ' ':
            wc += 1

    # TODO: fix word count functionality
    # TODO: add syllable count functionality

    return lc, wc, cc, sc


if __name__ == "__main__":
    print(wc())
