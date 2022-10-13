#outline of classes
import random


SUITS = ['♠️','♥️','♣️','♦️']
RANKS_VALUE = {
    'K': 10,
    'Q': 10,
    'J': 10,
    'A': 11,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
} 

class Game:
    def __init__(self):
        self.deck = Deck('Bycicle')
        self.deck.shuffle()
        self.player = Player()
        self.dealer = Dealer()
        #deal 2 cards to dealer and player
        self.deal(self.dealer)
        self.deal(self.player)
        self.deal(self.dealer)
        self.deal(self.player)
        print("The dealer's cards are: ")
        for card in self.dealer.hand:
            print(card)
            
        print(f'This hand is worth {self.calculate_hand(self.dealer)}')

        print("The Player's cards are: ")
        for card in self.player.hand:
            print(card)
            
        print(f'This hand is worth {self.calculate_hand(self.player)}')

        print(f"There are now {len(self.deck.cards)} cards in the deck.")

    def __str__(self):
        pass

    def deal(self, participant):
        card = self.deck.cards.pop()
        participant.hand.append(card)

    def calculate_hand(self, participant):
        total_points = 0
        for card in participant.hand:
            total_points += card.value
        return total_points
            
            



class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    
    def __str__(self):
        return f'{self.rank} of {self.suit}'





class Deck:
    def __init__(self, brand):
        self.cards = []
        self.brand = brand
        self.used = False
        for suit in SUITS:
            for rank in RANKS_VALUE.items():
                self.cards.append(Card(suit, rank[0], rank[1]))
    
    def __str__(self):
        return f'{self.brand} deck of {len(self.cards)} cards'

    def shuffle(self):
        for x in range(3):
            random.shuffle(self.cards)

# deck = Deck('Bicycle')
# deck.shuffle()
# for card in deck.cards:
#     print(card)

class Player:
    def __init__(self):
        self.hand = []



class Dealer:
    def __init__(self):
        self.hand = []


def End_Game (dealerValue, playerValue):
    if playerValue > dealerValue:
        print(f"Congradulations!! You beat the dealer with {playerValue} to their {dealerValue}")
    elif playerValue == dealerValue:
        print(f"It's a push both you and the dealer had {playerValue}")
    else:
        print(f"The dealer has won with {dealerValue} to your {playerValue}")






new_game = Game()
#Dealer code
if new_game.calculate_hand(new_game.dealer) == 21:
    print('Dealer had blackjack!')
    if new_game.calculate_hand(new_game.player) == 21:
        print('Push')
    else:
        print(f'You lose with {new_game.calculate_hand(new_game.player)}')
elif new_game.calculate_hand(new_game.player) == 21:
    print("Blackjack! You win!")
while new_game.calculate_hand(new_game.dealer) < 17:
    new_game.deal(new_game.dealer)
    if new_game.calculate_hand(new_game.dealer) > 21:
        print(f"Dealer has busted with {new_game.calculate_hand(new_game.dealer)}")
        
    elif new_game.calculate_hand(new_game.dealer) == 21:
        print("Dealer has 21!")
    
    else:
        print(f"The dealer's hand is :")
        [print(card) for card in new_game.dealer.hand]
        print(f"Worth: {new_game.calculate_hand(new_game.dealer)}")


print("Players hand is: ")
[print(card) for card in new_game.player.hand]

#player code
checked = False
playerBust = False
while(checked == False):
    choice = input("would you like to (h)it or (s)tay?").lower()
    if choice == 'h':
        checked = True
    elif choice == 's':
        break
    else:
        print("ERROR: INCORECT INPUT. Please enter 'h' or's'")

while checked and new_game.calculate_hand(new_game.player) < 21:
    new_game.deal(new_game.player)
    print("Players hand is: ")
    [print(card) for card in new_game.player.hand]
    print(f"Worth: {new_game.calculate_hand(new_game.player)}")

    if new_game.calculate_hand(new_game.player) > 21:
        print("player busted!")
        break
    elif new_game.calculate_hand(new_game.player) == 21:
        print('Player has made it to 21!')
        End_Game(new_game.calculate_hand(new_game.dealer), new_game.calculate_hand(new_game.player))
        

    choice = input("Would you like to (h)it or (s)tay?")


if choice == 's':
    print(f"Player stands with {new_game.calculate_hand(new_game.player)}")
    End_Game(new_game.calculate_hand(new_game.dealer), new_game.calculate_hand(new_game.player))




