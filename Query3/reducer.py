import fileinput
current = None
prev = None
count = 0
with fileinput.input() as finput:
    for line in finput:
        line = line.strip()
        sender, reciever = line.split(' ')
        if current == None:
            current = sender
        else:
            prev = current
            current = sender
            if current == prev:
                count = count + 1
            else:
                print(prev, count+1)
                count = 0
    print(sender, count+1)
