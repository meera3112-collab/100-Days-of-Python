
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_cards(deck, number_of_cards):
    for i in range(number_of_cards):
        deck.append(random.choice(cards))


def deck_sum(deck):
    score = sum(deck)

    while score > 21 and 11 in deck:
        deck.remove(11)
        deck.append(1)
        score = sum(deck)

    return score


def compare(player_score, dealer_score):

    if player_score == dealer_score:
        return "Match is Draw !!!"
    elif player_score > 21:
        return "You lost 😭"
    elif dealer_score > 21:
        return "You won!!! 😁"
    elif player_score == 21:
        return "You won!!! 😎"
    elif dealer_score == 21:
        return "You lost 😤"
    elif player_score > dealer_score:
        return "You won!!!"
    else:
        return "You lost"


def blackjack():
    print(logo)

    player_card = []
    dealer_card = []

    is_game_over = False

    draw_cards(player_card, 2)
    draw_cards(dealer_card, 2)

    while not is_game_over:

        player_score = deck_sum(player_card)
        dealer_score = deck_sum(dealer_card)

        print(f"Your cards: {player_card}, current score: {player_score}")
        print(f"Computer's first card: {dealer_card[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True

        else:
            should_player_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            if should_player_deal == 'y':
                draw_cards(player_card, 1)
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        draw_cards(dealer_card, 1)
        dealer_score = deck_sum(dealer_card)

    player_score = deck_sum(player_card)
    dealer_score = deck_sum(dealer_card)

    print(f"Your final hand: {player_card}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_card}, final score: {dealer_score}")

    print(compare(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    print("\n" * 20)
    blackjack()
