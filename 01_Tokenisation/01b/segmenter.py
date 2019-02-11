# LING-L 445: Practical 1B
# Dante Razo, drazo
import sys, codecs


def segmenter():
    print(sys.stdin.read().replace('. ', '.\n'))


def segmenterRU():
    corpus = codecs.open("russian.txt", "r", encoding="cp1251")  # russian encoding: cp1251
    output = codecs.open("russian-segmented.txt", "w", encoding="cp1251")  # create new file for output

    output.write(corpus.read().replace('.', '. \n'))  # NOTE: doesn't work with '. ', unsure why
    corpus.close()
    output.close()


if __name__ == "__main__":
    if not sys.stdin.isatty():
        segmenter()
    else:
        segmenterRU()
