import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = [r + " of " + s for s in suits for r in ranks]
random.shuffle(deck)

for i in range(1, 6):
    print("Attempt", i, ":", deck[i - 1])
