import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_card(self, card):
        self.hand.append(card)

    def get_sum(self):
        sum = 0
        ace_count = 0
        for card in self.hand:
            sum += card.value
            if card.rank == 'Ace':
                ace_count += 1

        while ace_count > 0 and sum > 21:  # Ace 처리
            sum -= 10
            ace_count -= 1

        return sum

    def show_hand(self):
        print(f"{self.name}의 현재 카드:")
        for card in self.hand:
            print(card)

    def is_bust(self):
        return self.get_sum() > 21


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.game_state = "Player Turn"

    def get_input(self, choices):
        while True:
            choice = input(f"선택하세요: {choices}")
            if choice in choices:
                return choice
            else:
                print("잘못된 입력입니다. 다시 입력부탁")

    def player_turn(self):
        while True:
            self.player.show_hand()
            if self.player.is_bust():
                print("Player BUSTED!")
                self.game_state = "Dealer Wins"
                break
            elif self.player.get_sum() == 21:
                print("Blackjack!")
                self.game_state = "Player Wins"
                break
            else:
                choice = self.get_input(["1", "2"])
                if choice == "1":
                    card = self.deck.deal()
                    self.player.take_card(card)
                elif choice == "2":
                    self.game_state = "Dealer Turn"
                    break

    def dealer_turn(self):
        while True:
            self.dealer.show_hand()
            if self.dealer.is_bust():
                print("Dealer BUSTED!")
                self.game_state = "Player Wins"
                break
            elif self.dealer.get_sum() == 21:
                print("Blackjack!")
                self.game_state = "Dealer Wins"
                break
            elif self.dealer.get_sum() >= 17:
                if self.player.get_sum() > self.dealer.get_sum():
                    self.game_state = "Player Wins"
                elif self.player.get_sum() < self.dealer.get_sum():
                    self.game_state = "Dealer Wins"
                else:
                    self.game_state = "Draw"
                break
            else:
                card = self.deck.deal()
                self.dealer.take_card(card)

    def play_game(self):
        print("게임 시작!")
        self.player.take_card(self.deck.deal())
        self.dealer.take_card(self.deck.deal())
        self.player.take_card(self.deck.deal())
        self.dealer.take_card(self.deck.deal())

        while True:
            if self.game_state == "Player Turn":
                self.player_turn()
            elif self.game_state == "Dealer Turn":
                self.dealer_turn()
            else:
                print(f"게임 결과: {self.game_state}")
                return


game = Blackjack()
game.play_game()