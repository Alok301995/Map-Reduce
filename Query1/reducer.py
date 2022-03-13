import fileinput
output = [0] * 1004
with fileinput.input() as finput:
    for line in finput:
        line = line.strip()
        sender, reciever = line.split(' ')
        output[int(sender)] = output[int(sender)] + 1
    for i in range(0, 1004):
        if output[i] > 0:
            print(i, output[i])
