from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts


def stripping(word):
    word = word.strip(".")
    word = word.strip(",")
    word = word.strip('"')
    word = word.strip(";")
    return word


def stringret(d_words):
    string = ""
    m = max(d_words.values())
    for key, value in d_words.items():
        if value > (m - 3):
            string += "<b>" + str(key) + "\t" + str(value) + "</b><br>"
        else:
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

YOUR_TEXT = " "

for word in testwords:
    YOUR_TEXT += word + " "

tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=170)

create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

message = '<html><head></head><body><img src= "cloud_large.png"></body></html>'

f1.write(message)

f1.close()
