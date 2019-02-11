# LING-L 445 - Practical 01a
# Dante Razo, drazo
from nltk.tokenize import sent_tokenize

# sample code, not mine
def maxmatch(wiki, words):
    fifty = wiki.read().strip("<onlyinclude>").split(":\n")[1:50]

    return fifty


def nltk(w):
    sample_text = "this's a sent tokenize test. this is sent two. is this sent three? sent 4 is cool! Now it’s your turn."
    sent_tokenize_list = sent_tokenize(sample_text)
    print("NLTK1: %f, %s\n", len(sent_tokenize_list), sent_tokenize_list)

    my_tokenize_list = sent_tokenize(w.read())
    print("NLTK2: %f, %s\n", len(my_tokenize_list), my_tokenize_list)


if __name__ == "__main__":
    wiki = open("wiki.txt", "r", encoding="utf8")
    words = open("wiki.words", "r", encoding="utf8")

    tokens = maxmatch(wiki, words)
    print(tokens)
    nltk(wiki)
