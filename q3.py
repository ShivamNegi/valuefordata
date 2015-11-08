def stripping(word):
    word = word.strip(".")
    word = word.strip(",")
    word = word.strip('"')
    word = word.strip(";")
    return word

testwords = []
checkwords = []

with open("test.txt", "r") as f1:
    for line in f1.readlines():
        line = line.split()
        for word in line:
            word = stripping(word)
            for w in word.split('.'):
                w = stripping(w)
                testwords.append(w)


with open("noise.txt", "r") as f2:
    for line in f2.readlines():
        line = line.split()
        for word in line:
            word = stripping(word)
            checkwords.append(word)

for word in testwords:
    if word not in checkwords:
        print word
