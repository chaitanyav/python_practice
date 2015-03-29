import math
import random
import time

def max_heapify(array, start, end):
    left = 2 * start + 1
    right = 2 * start + 2
    largest = start

    if left < end and array[left] > array[largest]:
        largest = left
    if right < end and array[right] > array[largest]:
        largest = right
    if largest != start:
        array[start], array[largest] = array[largest], array[start]
        max_heapify(array, largest, end)


def build_max_heap(array, start, end):
    mid = int(math.floor(float(end) / 2))
    for i in xrange(mid, -1, -1):
        max_heapify(array, i, end)

def heap_sort(array):
    end = len(array)
    build_max_heap(array, 0, end)
    while end > 0:
        max_heapify(array, 0, end)
        end = end - 1
        array[0], array[end] = array[end], array[0]


for item in [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800]:
    array = range(item)
    random.shuffle(array)

    start_time = time.time()
    heap_sort(array)
    print "Time taken by heap sort with N: %d random order is %f sec" % (item, time.time() - start_time)

    start_time = time.time()
    heap_sort(array)
    print "Time taken by heap sort with N: %d sorted order is %f sec" % (item, time.time() - start_time)

    array.reverse()
    start_time = time.time()
    heap_sort(array)
    print "Time taken by heap sort with N: %d reverse sorted order is %f sec" % (item, time.time() - start_time)
