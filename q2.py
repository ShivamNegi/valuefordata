count = 0

with open("test.txt", "r") as f1:
    for line in f1.readlines():
        line = line.split()
        # 179 words as on".Something is another word
        for word in line:
            if word[1:len(word) - 1].count('"') > 0:
                count += 1
        count += len(line)

print count
