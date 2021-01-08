import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, bot_score):
    if player_score > 21 and bot_score > 21:
        return "You lose"

    if player_score == bot_score:
        return "Draw"
    elif bot_score == 0:
        return "You lose"
    elif player_score == 0:
        return "You win"
    elif player_score > 21:
        return "You lose"
    elif bot_score > 21:
        return "You win"
    elif player_score > bot_score:
        return "You win"
    else:
        return "You lose"

def play_game():

    player_cards = []
    bot_cards = []
    game_over = False
    for _ in range(2):
        player_cards.append(deal_card())
        bot_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        bot_score = calculate_score(bot_cards)
        print(f"Your card is :{player_cards}, your current score is {player_score}")
        print(f"Bot's first card is {bot_cards[0]}")

        if player_score == 0 or bot_score == 0 or player_score > 21:
            game_over = True
        else:
            ask = input("another card? 'y' or 'n'\n")
            if ask == "y":
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
            else:
                game_over = True

    while bot_score != 0 and bot_score < 17:
        bot_cards.append(deal_card())
        print("Added a card to bot")
        bot_score = calculate_score(bot_cards)

    print()
    print(f"Your cards are {player_cards}, your final score is {player_score}.")
    print(f"Bot's has {bot_cards}, bot's final score is {bot_score}")
    print(compare(player_score, bot_score))

while str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")) == "y":
    play_game()