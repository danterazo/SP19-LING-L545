import sys


def wc():
    # returns (line count, word count, character count
    lc, wc, cc = 0, 0, 0

    # counting; space delimiter for words
    for c in sys.stdin.read():
        cc += 1
        if c is '\n':
            lc += 1
        elif c is ' ':
            wc += 1

    return lc, wc, cc


if __name__ == "__main__":
    print(wc())
