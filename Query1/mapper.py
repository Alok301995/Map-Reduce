file = open('network.txt', 'r')
for line in file:
    line = line.strip()
    sender, reciever = line.split(' ')
    if sender != reciever:
        print(int(sender), int(reciever))
file.close()
