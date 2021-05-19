def sort(data):
    h = 1
    while h < len(data) / 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, len(data)):
            for j in range(i, h - 1, -h):
                if data[j] < data[j - h]:
                    data[j], data[j - h] = data[j - h], data[j]
                else:
                    break
        h = h // 3


import random
import time

if __name__ == "__main__":
    data = []
    for j in range(10):
        data.append(random.randint(1, 100000))
    print(data)
    sort(data)
    print(data)

    i = 10
    data = []
    while i < 100000000:
        for j in range(i):
            data.append(random.randint(1, 100000))
        start_time = time.time()
        sort(data)
        print(i, ": %s seconds ---" % (time.time() - start_time))
        i = i * 2
        data.clear()
