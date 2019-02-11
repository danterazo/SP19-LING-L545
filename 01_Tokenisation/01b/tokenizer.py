# LING-L 445: Practical 1B
# Dante Razo, drazo
import sys


def tokenizer():
    print(sys.stdin.read().replace(' ', '\n'))


if __name__ == "__main__":
    tokenizer()
