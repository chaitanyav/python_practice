

import random
import time
import sys


sys.setrecursionlimit(1000000)

def partition(numbers, low, high):
    pivot_index = low + (high - low) / 2
    pivot_value = numbers[pivot_index]
    numbers[high], numbers[pivot_index] = numbers[pivot_index], numbers[high]
    pivot_index = low

    for index in xrange(low, high):
        if numbers[index] < pivot_value:
            numbers[index], numbers[pivot_index] = numbers[pivot_index], numbers[index]
            pivot_index += 1

    numbers[pivot_index], numbers[high] = numbers[high], numbers[pivot_index]
    return pivot_index


def quick_sort(numbers, low, high):
    if low < high:
        pivot_index = partition(numbers, low, high)
        quick_sort(numbers, low, pivot_index - 1)
        quick_sort(numbers, pivot_index + 1, high)

for item in [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800]:
    numbers = range(item)
    random.shuffle(numbers)

    start_time = time.time()
    quick_sort(numbers, 0, item - 1)
    print "Time taken by quick sort with %d elements, random order: %f" % (item, time.time() - start_time)

    start_time = time.time()
    quick_sort(numbers, 0, item - 1)
    print "Time taken by quick sort with %d elements, sorted order: %f" % (item, time.time() - start_time)

    numbers.reverse()
    start_time = time.time()
    quick_sort(numbers, 0, item - 1)
    print "Time taken by quick sort with %d elements, reverse sorted order: %f" % (item, time.time() - start_time)
