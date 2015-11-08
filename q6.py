def stripping(word):
    word = word.strip(".")
    word = word.strip(",")
    word = word.strip('"')
    word = word.strip(";")
    return word


def stringret(d_words):
    string = ""
    for key, value in d_words.items():
        string += str(key) + "\t" + str(value) + "<br>"
    return string

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

d_words = {}
for word in testwords:
    if word not in checkwords:
        d_words[word] = testwords.count(word)

print d_words

f1 = open("table.html", 'w')

message = "<html><head></head><body>" + stringret(d_words) + "</body></html>"

f1.write(message)

f1.close()
