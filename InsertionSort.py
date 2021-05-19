def sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
            else:
                break


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
        i = i * 5
        data.clear()
