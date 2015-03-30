import random

def fisher_yates(array):
    length = len(array)
    for i in xrange(0, length):
        j = random.randint(i, length - 1)
        array[i], array[j] = array[j], array[i]


SUITS = [u'\u2660', u'\u2665', u'\u2666', u'\u2663']
CARDS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J']


deck = [card + suit for suit in SUITS for card in CARDS]
fisher_yates(deck)
for index, card in enumerate(deck):
    print card,
    if (index + 1) % 13 == 0:
        print
