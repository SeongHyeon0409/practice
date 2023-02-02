import random

# deck of cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

# deal two cards to player
player = [random.choice(deck), random.choice(deck)]
deck.remove(player[0])
deck.remove(player[1])

# deal two cards to dealer
dealer = [random.choice(deck), random.choice(deck)]
deck.remove(dealer[0])
deck.remove(dealer[1])

# player's turn
while sum(player) < 21:
    print("Player's hand:", player)
    print("Player's total:", sum(player))
    action = input("Hit or Stand? (h/s)").lower()
    if action == "h":
        player.append(random.choice(deck))
        deck.remove(player[-1])
        if sum(player) > 21:
            print("Player busts!")
            break
    else:
        break

# dealer's turn
while sum(dealer) < 17:
    print("dealer's deck :", dealer)
    dealer.append(random.choice(deck))
    deck.remove(dealer[-1])

print("Dealer's hand:", dealer)
print("Dealer's total:", sum(dealer))

# determine the winner
if sum(player) > 21:
    print("Dealer wins!")
elif sum(dealer) > 21:
    print("Player wins!")
elif sum(player) > sum(dealer):
    print("Player wins!")
elif sum(dealer) > sum(player):
    print("Dealer wins!")
else:
    print("Tie!")