import random
import time

def partition(array, low, high):
    pivot_index = low + (high - low) / 2
    pivot_value = array[pivot_index]
    array[pivot_index], array[high] = array[high], array[pivot_index]
    pivot_index = low

    for index in xrange(low, high):
        if array[index] < pivot_value:
            array[index], array[pivot_index] = array[pivot_index], array[index]
            pivot_index += 1


    array[pivot_index], array[high] = array[high], array[pivot_index]
    return pivot_index


def quick_select(array, low, high, n):

    if low == high:
        return array[low]

    pivot_index = partition(array, low, high)

    if n == pivot_index:
        return array[pivot_index]
    elif n < pivot_index:
        return quick_select(array, low, pivot_index - 1, n)
    else:
        return quick_select(array, pivot_index + 1, high, n)



for item in [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800]:
    array = range(item)
    random.shuffle(array)
    start_time = time.time()
    k = 5
    kth_smallest = quick_select(array, 0, item - 1, k - 1)
    print "%dth smallest is %d, Time taken to find the %dth smallest value is %f sec" % (k, kth_smallest, k, time.time() - start_time)
