# LING-L 445: Practical 1B
# Dante Razo, drazo
import sys, codecs


def tokenizer():
    print(sys.stdin.read().replace(' ', '\n'))


if __name__ == "__main__":
    tokenizer()
