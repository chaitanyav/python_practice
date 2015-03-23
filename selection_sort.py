import random
import time

def minimum_index(numbers, lindex, n):
    min_index = None
    for index in xrange(lindex, n):
        if min_index is None:
            min_index = index
        else:
            if numbers[min_index] > numbers[index]:
                min_index = index
    return min_index


def selection_sort(numbers):
    n = len(numbers)
    for index in xrange(n):
        min_index = minimum_index(numbers, index, n)
        numbers[index], numbers[min_index] = numbers[min_index], numbers[index]

    return numbers

for elem in [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]:
    numbers = range(elem)

    random.shuffle(numbers)
    start_time = time.time()
    numbers = selection_sort(numbers)
    print "Time for selection sort with %d elements random order: %f (sec)" % (elem, time.time() - start_time)

    start_time = time.time()
    numbers = selection_sort(numbers)
    print "Time for selection sort with %d elements sorted order: %f (sec)" % (elem, time.time() - start_time)

    start_time = time.time()
    numbers.reverse()
    numbers = selection_sort(numbers)
    print "Time for selection sort with %d elements reverse sorted order: %f (sec)" % (elem, time.time() - start_time)
    #print numbers
