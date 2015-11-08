def stripping(word):
    word = word.strip(".")
    word = word.strip(",")
    word = word.strip('"')
    word = word.strip(";")
    return word


testwords = []

with open("test.txt", "r") as f1:
    for line in f1.readlines():
        line = line.split()
        for word in line:
            word = stripping(word)
            for w in word.split('.'):
                w = stripping(w)
                testwords.append(w)

d = {}
for word in testwords:
    d[word] = testwords.count(word)

print d
