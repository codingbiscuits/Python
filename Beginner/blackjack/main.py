import os
import random
from art import logo


def deal_card():
    """Picks a random card from the list and returns it"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(card_list):
    """Take a list of cards, adds them all up, and then returns the sum"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def compare_scores(score1, score2):
    """Takes in user score as first input and computer score as second input and checks the winner"""
    if score1 == score2:
        print(f"It's a draw! Your score: {score1}. Computer score: {score2}.")
    elif score2 == 0:
        print(
            f"You lose! The computer got a Blackjack! Your score: {score1}. Computer score: {score2}.")
    elif score1 == 0:
        print(
            f"Blackjack! You win! Your score: {score1}. Computer score: {score2}.")
    elif score1 > 21:
        print(
            f"You went over, you lose!  Your score: {score1}. Computer score: {score2}.")
    elif score2 > 21:
        print(
            f"Computer went over. You win! Your score: {score1}. Computer score: {score2}.")
    elif score1 > score2:
        print(f"You win! Your score: {score1}. Computer score: {score2}.")
    else:
        print(f"You lose! Your score: {score1}. Computer score: {score2}.")


def play_blackjack():

    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(
            f"Your cards: {user_cards}. Current score: {calc_score(user_cards)}.")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input(
                "Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    compare_scores(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    os.system("clear")
    play_blackjack()
