import random


def rank_hand(hand):
    """
    Function to rank a five card hand
    :param hand: list of 5 integers representing card values
    :return: integer representing the rank of the hand
    """
    # Check for straight flush
    if len(set([x // 10 for x in hand])) == 1 and len(set(hand)) == 5:
        return 9

    # Check for four of a kind
    for i in set(hand):
        if hand.count(i) == 4:
            return 8

    # Check for full house
    if len(set(hand)) == 2:
        return 7

    # Check for flush
    if len(set([x // 10 for x in hand])) == 1:
        return 6

    # Check for straight
    if len(set(hand)) == 5:
        if max(hand) - min(hand) == 4:
            return 5

    # Check for three of a kind
    for i in set(hand):
        if hand.count(i) == 3:
            return 4

    # Check for two pair
    pair_count = 0
    for i in set(hand):
        if hand.count(i) == 2:
            pair_count += 1
    if pair_count == 2:
        return 3

    # Check for one pair
    for i in set(hand):
        if hand.count(i) == 2:
            return 2

    # If none of the above, return highest card
    return 1


def compare_hands(hand1, hand2):
    """
    Function to compare two hands and determine the winner
    :param hand1: list of 5 integers representing card values
    :param hand2: list of 5 integers representing card values
    :return: 0 if tie, 1 if hand1 wins, 2 if hand2 wins
    """
    rank1 = rank_hand(hand1)
    rank2 = rank_hand(hand2)

    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return 2
    else:
        return 0


# Create deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# Shuffle deck and deal hands to player and computer
random.shuffle(deck)
player_hand = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()]
computer_hand = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()]

# Compare hands and determine winner
result = compare_hands(player_hand, computer_hand)
print("player's hand :", player_hand)
print("computer's hand :", computer_hand)

if result == 1:
    print("Player wins with a", rank_hand(player_hand), "hand!")
elif result == 2:
    print("Computer wins with a", rank_hand(computer_hand), "hand!")
else:
    print("Tie!")