class FrenchDeck:

    @staticmethod
    def deck():
        card_deck = []
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for card in cards:
                    card_deck.append(suit+'-'+card)
        return card_deck