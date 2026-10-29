import random
from french_deck import FrenchDeck
import time


def player_hit(counter_player, session_deck, card_history):
    random_selection = random.randint(0,len(session_deck))
    drawn_card = session_deck[random_selection]
    card_amount = drawn_card.split('-')[1]
    session_deck.pop(random_selection)
    card_history.append(card_amount)
    print(drawn_card)
    print(card_history)

    if card_amount not in ['Jack', 'Queen', 'King','A']:
        counter_player += int(card_amount)
        if counter_player > 21:
            if 'A' in card_history:
                counter_player -= 10
            else:
                print("You have scored over 21. \n You have lost.")

    elif card_amount in ['Jack', 'Queen', 'King']:
        counter_player += 10
        if counter_player > 21:
            if 'A' in card_history:
                counter_player -= 10
            else:
                print("You have scored over 21. \n You have lost.")

    else:

        if (counter_player + 11 > 21) and counter_player< 21:
            counter_player += 1

        elif (counter_player+ 11 < 21) and counter_player< 21:
            counter_player += 11

    return counter_player


if __name__ == '__main__':
    session_deck = FrenchDeck.deck()
    random.shuffle(session_deck)
    counter_bank = 0
    counter_player = 0
    card_history_bank = []
    card_history_player = []

    print("Welcome to Blackjack.", flush=True)
    time.sleep(3)
    print("Good luck, sir!", flush=True)

    while counter_bank or counter_player < 22:

        print("Hit or stay?")

        response = str(input()).lower()

        if response == 'hit':
            counter_player = player_hit(counter_player, session_deck, card_history_player)
            print(counter_player)


        # TODO: Add the actions for hit or stay for player and for bank.
        # Add randomness element to bank choosing hit or stay. likelihood increasing as counter approaches 21    


    if counter_player > 22:
        print("You have lost.")

    elif counter_bank > 22:
        print("The house lost. You have won.")

