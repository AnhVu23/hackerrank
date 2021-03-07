# Solution for word order challenge in Python using OrderedDict and Counter
from collections import OrderedDict, Counter
class OrderedCounter(OrderedDict):
    def __missing__(self, key):
        return 0

n = int(input().split()[0])
words = OrderedCounter()
for x in range(n):
    word = input()
    words[word] += 1
print(len(words))
print(*words.values())