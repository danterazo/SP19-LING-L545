# LING-L 445: Practical 1B
# Dante Razo, drazo
import sys


def preprocessing(x):  # replace certain punctiation characters with spaces
    x = x.replace(';', ' ')
    x = x.replace(':', ' ')
    x = x.replace('(', ' ')
    x = x.replace(')', ' ')
    return x


def tokenizer():
    return preprocessing(sys.stdin.read()).replace(' ', '\n')  # replaces spaces in preprocessed text with newline


if __name__ == "__main__":
    print(tokenizer())
