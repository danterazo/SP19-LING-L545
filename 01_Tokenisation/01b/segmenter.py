import sys, codecs, fileinput


def segmenter():
    print(sys.stdin.read().replace('. ', '.\n'))


def segmenterRU():
    corpus = open("russian.txt", "r")
    output = open("russian-segmented.txt", "w")

    output.write(corpus.read().replace('. ', '.\n'))
    # russian encoding: cp1251


if __name__ == "__main__":
    segmenterRU()
