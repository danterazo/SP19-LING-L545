import sys

counter = 0

for c in sys.stdin.read():
    if c == 'и':
        counter += 1
print(counter)
