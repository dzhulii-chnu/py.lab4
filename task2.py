from itertools import product

ranks = ['10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
point = {'10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def rank_value(rank):
    return point[rank]


def is_valid(pair):
    rank, suit = pair
    return rank_value(rank) % 2 == 0


pairs = product(ranks, suits)
valid_pairs = list(filter(is_valid, pairs))

print(valid_pairs)