# LING-L 445 Practical 04: Parsing
# Dante Razo, drazo, 4/14/2019
import matplotlib.pyplot as plt

labels = {0: 'zh', 1: 'fr', 2: 'de', 3: 'id', 4: 'ja', 5: 'ko', 6: 'pt', 7: 'ru', 8: 'es', 9: 'tr'}  # ISO 639.2
x = [0, 0, 0, 0, 0, 0, 0, 0.5, 0.4, 0.7]  # proportion of OV
y = [1 - c for c in x]  # proportion of VO
plt.plot(x, y, 'ro')
plt.title('Relative word order of verb and object')
plt.xlim([0, 1])  # Set the x and y axis ranges
plt.ylim([0, 1])
plt.xlabel('OV')  # Set the x and y axis labels
plt.ylabel('VO')
for i in labels:  # Add labels to each of the points
    plt.text(x[i] - 0.03, y[i] - 0.03, labels[i], fontsize=9)

plt.savefig("rwo.PNG")
plt.show()
