def sort(my_data):
    for i, _ in enumerate(my_data):
        min_el = i
        for j in range(i + 1, len(my_data)):
            if my_data[j] < my_data[min_el]:
                min_el = j
        my_data[i], my_data[min_el] = my_data[min_el], my_data[i]


import random
import time

if __name__ == "__main__":
    i = 10
    data = []
    while i < 100000000:
        for j in range(i):
            data.append(random.randint(1, 100000))
        start_time = time.time()
        sort(data)
        print(i, ": %s seconds ---" % (time.time() - start_time))
        i = i + 100
        data.clear()