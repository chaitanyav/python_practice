import random
import sys
import time

#sys.setrecursionlimit(100000)

def merge(numbers, low, mid, high):
    left = []
    right = []
    for i in xrange(low, mid + 1):
        left.append(numbers[i])
    for i in xrange(mid + 1, high + 1):
        right.append(numbers[i])

    i = 0
    j = 0
    k = low
    while True:
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numbers[k] = left[i]
                k += 1
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
                k += 1
        else:
            break

    while i < len(left) and k < (high + 1):
        numbers[k] = left[i]
        k += 1
        i += 1
    while j < len(right) and k < (high + 1):
        numbers[k] = right[j]
        k += 1
        j += 1

def merge_sort(numbers, low, high):
    if low < high:
        mid = low + (high - low) / 2
        merge_sort(numbers, low, mid)
        merge_sort(numbers, mid + 1, high)
        merge(numbers, low, mid, high)

for item in [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800]:
    numbers = range(item)
    random.shuffle(numbers)
    start_time = time.time()
    merge_sort(numbers, 0, item - 1)
    print "Time taken by merge sort with %d elements, random order: %f" % (item, time.time() - start_time)

    start_time = time.time()
    merge_sort(numbers, 0, item - 1)
    print "Time taken by merge sort with %d elements, sorted order: %f" % (item, time.time() - start_time)

    numbers.reverse()
    start_time = time.time()
    merge_sort(numbers, 0, item - 1)
    print "Time taken by merge sort with %d elements, reverse sorted order: %f" % (item, time.time() - start_time)
