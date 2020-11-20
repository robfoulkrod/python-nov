import random


suits = "C D S H".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()

cards = [(rank, suit) for rank in ranks for suit in suits]

random.shuffle(cards)

for _ in range(5):
    print(cards.pop())
