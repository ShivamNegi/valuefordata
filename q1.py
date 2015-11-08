f1 = open("test.txt")

count = 0

for line in f1.readlines():
    count += 1

f1.close()

print count
