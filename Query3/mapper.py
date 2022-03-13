from io import SEEK_SET
result = open('../Query2/result.txt', 'r')
network_file = open('network.txt', 'r')

for line2 in network_file:
    line2 = line2.strip()
    s, receiver = line2.split(' ')
    for line1 in result:
        line1 = line1.strip()
        sender, _ = line1.split(' ')
        if sender == receiver:
            print(sender, s)
    result.seek(SEEK_SET)

result.close()
network_file.close()
