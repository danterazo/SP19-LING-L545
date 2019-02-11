import sys, codecs, fileinput


def segmenter():
    print(sys.stdin.read().replace('. ', '.\n'))


def segmenterRU():
    corpus = codecs.open("russian.txt", "r", encoding="cp1251")  # russian encoding: cp1251
    codecs.open("russian-segmented.txt", "w").writelines(
        [l for l in open("russian.txt").readlines()])  # copy input -> output

    # segment new file by replacing full stops with newlines
    with fileinput.FileInput("russian-segmented.txt", inplace=True) as file:
        for line in file:
            print(line.replace('.', '.\n'), end='')  # TODO: doesn't work when replacing '. '; using temp fix

    # print(output.read().replace('. ', '.\n'))
    # output.write(output.read().replace('. ', '.\n'))
    # russian encoding: cp1251

    corpus.close()

    # CLOSE files


if __name__ == "__main__":
    segmenterRU()
