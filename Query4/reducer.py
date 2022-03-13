import fileinput
prev = None
count = 0
max = (0, 0)

with fileinput.input() as finput:
    for line in finput:
        line = line.strip()
        sender, reciever = line.split(' ')
        if prev == None:
            prev = sender
            count = count+1
        else:
            if sender != prev:
                if count > max[1]:
                    max = (prev, count)
                count = 1
                prev = sender
            else:
                count = count+1
                prev = sender

print(max[0], max[1])
