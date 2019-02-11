import sys, codecs


def segmenter():
    print(sys.stdin.read().replace('. ', '.\n'))


def segmenterRU():
    corpus = codecs.open("russian.txt", "r", encoding="cp1251")  # russian encoding: cp1251
    output = codecs.open("russian-segmented.txt", "w", encoding="cp1251")  # create new file for output

    output.write(corpus.read().replace('.', '. \n'))
    corpus.close()
    output.close()


if __name__ == "__main__":
    segmenterRU()
