# LING-L 445 - Practical 01a
# Dante Razo, drazo
from nltk.tokenize import sent_tokenize


def maxmatch(wiki, words):
    fifty = wiki.read().strip("<onlyinclude>").split(":\n")[1:50]

    print("file:", fifty)


def nltk():
    text = "testing. testing. testing!"
    sent_tokenize_list = sent_tokenize(text)
    len(sent_tokenize_list)
    sent_tokenize_list
    # > import nltk
    # > nltk.download()


if __name__ == "__main__":
    wiki = open("wiki.txt", "r", encoding="utf8")
    words = open("wiki.words", "r", encoding="utf8")

    tokens = maxmatch(wiki, words)
    print(tokens)
    nltk()
