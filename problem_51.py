
import math
import cProfile


def prime_sieve(n):
    numbers = [True] * n
    numbers[0:2] = [False, False]
    root = math.floor(math.sqrt(n))

    for number1 in xrange(2, n, 1):
        if not numbers[number1]:
            continue
        if number1 > root:
            break
        if number1 == 2:
            number2 = 2
        else:
            number2 = 3
        product = number1 * number2
        while product < n:
            if product % number1 == 0 and numbers[product]:
                numbers[product] = False
            if number1 == 2:
                number2 += 1
            else:
                number2 += 2
            product = number1 * number2

    return numbers

pr = cProfile.Profile()
pr.enable()
print len(filter(lambda l: l is True, prime_sieve(1000000000)))
pr.disable()
pr.print_stats()