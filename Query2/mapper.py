file = open('../Query1/result.txt', 'r')
for line in file:
    line = line.strip()
    sender, count = line.split(' ')
    print(int(sender), int(count))
file.close()
