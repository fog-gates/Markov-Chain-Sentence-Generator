testTxt = "the theremin is theirs, ok? This is a theremin. This is not anything but a theremin."
nGrams = []
nextChar = []
import random

#Creates the nGram object which stores the necessary information
class nGram:
    def __init__(self, name, count, next):
        self.ngram = name
        self.count = count
        next = [next]
        self.nextChar = next
    def __repr__(self):
        return(str(self.ngram) + "-" + str(self.count) + "-" + str(self.nextChar))
    def __eq__(self, other):
        return self.ngram == other.ngram


i = 0
while i < len(testTxt):

    if i + 3 < len(testTxt):
        gram = nGram(testTxt[i:i + 3], 1, testTxt[i + 3])
    else:
        break

    if gram in nGrams:
        nGrams[nGrams.index(gram)].count += 1
        nGrams[nGrams.index(gram)].nextChar.append(testTxt[i + 3])
        nGrams.append(gram)
    else:
        nGrams.append(gram)

    i += 3

print(nGrams)

k = 0
while k < 10:
    a = random.randint(0, len(nGrams) - 1)
    b = random.randint(0, len(nGrams[a].nextChar) - 1)
    print(nGrams[a].ngram + nGrams[a].nextChar[b])
    k += 1