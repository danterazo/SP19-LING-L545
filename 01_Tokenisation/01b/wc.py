import sys

"""
TODO:
- Fix word count
- Syllable count
"""


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

    return lc, wc, cc, sc


if __name__ == "__main__":
    print(wc())
