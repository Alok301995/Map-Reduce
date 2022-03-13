dept_file = open('dept_labels.txt', 'r')
network = open('network.txt', 'r')
dept_id = []

for line in dept_file:
    line = line.strip()
    _, dept = line.split(' ')
    dept_id.append(dept)
dept_file.close()


for line in network:
    line = line.strip()
    sender, receiver = line.split(' ')
    if dept_id[int(sender)] != dept_id[int(receiver)]:
        print(dept_id[int(sender)], 1)
network.close()
