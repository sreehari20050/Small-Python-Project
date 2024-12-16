import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 😐"
    elif c_score == 0:
        return "Opponent Has A Black Jack 😱"
    elif u_score == 0 :
        return "You Have A Black Jack 😱"
    elif u_score > 21:
        return "You Loose! , Computer Wins!!!"
    elif c_score > 21:
        return "You Win!"
    elif u_score > c_score:
        return "You Win!"
    else:
        return "You Lose!"

def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        print(art.logo)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Card : {user_cards}, Current Score: {user_score}")
        print(f"Computer Card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand : {user_cards}, Final Score : {user_score}")
    print(f"Computer Final Hand : {computer_cards}, Final Score : {computer_score}")
    print(compare(u_score=user_score,c_score=computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
