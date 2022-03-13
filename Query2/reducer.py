import fileinput
import math
c = 0
output = [None]*10

# -------------------Heap Implementation-----------------------


def percolate_up(arr, index):
    child = index
    parent = math.ceil(child/2) - 1
    while child != parent and parent != -1:
        if arr[parent][1] < arr[child][1]:
            arr[parent], arr[child] = arr[child], arr[parent]
            child = parent
            parent = math.ceil(child/2) - 1
        else:
            break


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l][1] > arr[largest][1]:
        largest = l

    if r < n and arr[r][1] > arr[largest][1]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def buildHeap(arr, n):
    startIdx = n // 2 - 1
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)


def modify_key(arr, key, n):
    smallest = None
    smallest_idx = None
    for i in range(math.floor(n/2), n):
        if smallest == None:
            smallest_idx = i
            smallest = arr[i][1]
        else:
            if smallest >= arr[i][1]:
                smallest_idx = i
                smallest = arr[i][1]
    if arr[smallest_idx][1] > key[1]:
        return
    else:
        arr[smallest_idx] = key
        percolate_up(arr, smallest_idx)


# --------------------------------------------------------
with fileinput.input() as finput:
    for line in finput:
        line = line.strip()
        sender, count = line.split(' ')
        if c < 10:
            output[c] = (int(sender), int(count))
        elif c == 10:
            buildHeap(output, 10)
            modify_key(output, (int(sender), int(count)), 10)
        else:
            modify_key(output, (int(sender), int(count)), 10)
        c = c+1

for i in output:
    print(i[0], i[1])
