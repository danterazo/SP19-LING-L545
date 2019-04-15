# LING-L 445 Practical 04: Parsing
# Dante Razo, drazo, 4/14/2019
import matplotlib.pyplot as plt
from conllu import parse_incr
from io import open

root = "data\\"


# returns OV proportion; VO can be calculated from that number outside the function
def rwo_proportion(datadir, code):
    type = "dev"  # choose development, training, or testing files
    ext = ".conllu"
    treebank = "gsd"
    ov_count = 0
    word_count = 0
    verbose = 1

    if datadir == "UD_Turkish-IMST":  # the one exception (IMST vs. GSD)
        treebank = "imst"

    dir = root + datadir + "\\" + code + "_" + treebank + "-ud-" + type + ext

    data = open(dir, "r", encoding="utf-8")

    for tokens in parse_incr(data):
        for c in tokens:
            word_count += 1

            if verbose is 2:
                print(c)  # VERY verbose; use for debugging purposes

            # NOTE: "OV if word_index is < head_index"
            if c["id"] and c["head"] and c["id"] < c["head"]:
                ov_count += 1

    ov_proportion = ov_count / word_count

    if verbose is 1:
        num_spaces = 17 - len(datadir)  # for cleaner console output formatting / presentation

        print("OV_proportion for " + datadir + ': ' + ''.join(' ' * num_spaces) + str(ov_proportion))
        print("VO_proportion for " + datadir + ': ' + ''.join(' ' * num_spaces) + str(1 - ov_proportion))

    return ov_proportion


""" the following is adapted from ftyers' example """
labels = {0: 'es', 1: 'fr', 2: 'de', 3: 'id', 4: 'ja', 5: 'ko', 6: 'pt', 7: 'ru', 8: 'tr', 9: 'zh'}  # ISO 639.2

# OV proportions below
es = rwo_proportion("UD_Spanish-GSD", "es")  # expected: 0.4 (from practical example)
fr = rwo_proportion("UD_French-GSD", "fr")
de = rwo_proportion("UD_German-GSD", "de")
id = rwo_proportion("UD_Indonesian-GSD", "id")
ja = rwo_proportion("UD_Japanese-GSD", "ja")
ko = rwo_proportion("UD_Korean-GSD", "ko")
pt = rwo_proportion("UD_Portuguese-GSD", "pt")
ru = rwo_proportion("UD_Russian-GSD", "ru")  # expected: 0.5
tr = rwo_proportion("UD_Turkish-IMST", "tr")  # expected: 0.7
zh = rwo_proportion("UD_Chinese-GSD", "zh")

x = [es, fr, de, id, ja, ko, pt, ru, tr, zh]  # add proportions to vector for easy iteration
y = [1 - c for c in x]  # proportion of VO
plt.plot(x[0::2], y[0::2], 'ro')  # evens are red
plt.plot(x[1::2], y[1::2], 'bo')  # odds are blue
plt.title('Relative Word Order of Verb and Object')

adjust = 0.05  # forces 0.5 stepping on axes and keeps graph focused and compact
plt.xlim([min(x) - adjust, max(x) + adjust])  # Set the x and y axis ranges
plt.ylim([min(y) - adjust, max(y) + adjust])
plt.xlabel('Object-Verb (OV)')  # Set the x and y axis labels
plt.ylabel('Verb-Object (VO)')

acc = -1  # just an accumulator
for i in labels:  # Add labels to each of the points
    acc += 1

    if (acc % 2) == 0:  # it's not pretty but it helps distinguish the crowded points in the center of the plot
        offset = 0.02
        color = "red"
    else:
        offset = -0.01
        color = "blue"

    plt.text(x[i] - offset, y[i] - offset, labels[i], bbox=dict(facecolor=color, alpha=0.2),
             fontsize=9)

plt.savefig("report_3assets//rwo.PNG")
plt.show()
