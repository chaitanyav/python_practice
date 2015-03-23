import random
import time

def insertion_sort(numbers):

    n = len(numbers)
    for index1 in xrange(n):
        index2 = index1
        while index2 > 0 and numbers[index2] < numbers[index2 - 1]:
            numbers[index2], numbers[index2 - 1] = numbers[index2 - 1], numbers[index2]
            index2 -= 1
    return numbers


for item in [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200]:
    numbers = range(item)
    random.shuffle(numbers)
    start_time = time.time()
    numbers = insertion_sort(numbers)
    print "Insertion sort with %d elements random order: %f sec" % (item, time.time() - start_time)

    start_time = time.time()
    numbers = insertion_sort(numbers)
    print "Insertion sort with %d elements sorted order: %f sec" % (item, time.time() - start_time)

    start_time = time.time()
    numbers.reverse()
    numbers = insertion_sort(numbers)
    print "Insertion sort with %d elements reversed sorted order: %f sec" % (item, time.time() - start_time)
