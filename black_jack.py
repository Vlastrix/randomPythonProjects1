import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

# RULES
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


# variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
gold_number = 21


# functions
def card_selector(pc_or_user):
    for card in range(2):
        selected_cards = random.choice(cards)
        if pc_or_user == "user":
            user_chosen_cards.append(selected_cards)
        elif pc_or_user == "pc":
            computer_chosen_cards.append(selected_cards)


def black_jack():
    global output, user_chosen_cards, computer_chosen_cards
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == "y":
        user_chosen_cards = []
        computer_chosen_cards = []
        card_selector("user")
        card_selector("pc")

        def black_jack_process_checker():
            global output, sum_score_user, sum_score_computer
            sum_score_user = sum(user_chosen_cards)
            sum_score_computer = sum(computer_chosen_cards)
            if sum_score_user == gold_number:
                return "blackjack_user"
            elif sum_score_computer == gold_number:
                return "blackjack_pc"
            if sum_score_user > gold_number:
                if 11 in user_chosen_cards:
                    index_of_11 = user_chosen_cards.index(11)
                    user_chosen_cards[index_of_11] = 1
                    sum_score_user = sum(user_chosen_cards)
                    if sum_score_user > gold_number:
                        return "lose"
                else:
                    return "lose"
            print(f"    Your cards: {user_chosen_cards}, current score: {sum_score_user}")
            print(f"    Computer's first card: {computer_chosen_cards[0]}")
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                user_chosen_cards.append(random.choice(cards))
                black_jack_process_checker()
            while sum_score_computer < 17:
                computer_chosen_cards.append(random.choice(cards))
                sum_score_computer = sum(computer_chosen_cards)
            if sum_score_user > gold_number:
                return "lose"
            elif sum_score_computer > gold_number:
                return "win"
            elif sum_score_computer > sum_score_user:
                return "lose"
            elif sum_score_computer < sum_score_user:
                return "win"
            elif sum_score_computer == sum_score_user:
                return "draw"

        output = black_jack_process_checker()
        if output == "win":
            print("You win!!!")
            print(f"    Your final hand: {user_chosen_cards} with a score of {sum_score_user}")
            print(f"    Computer's final hand: {computer_chosen_cards} with a score of {sum_score_computer}")
            black_jack()
        elif output == "lose":
            print("You lose!!!")
            print(f"    Your final hand: {user_chosen_cards} with a score of {sum_score_user}")
            print(f"    Computer's final hand: {computer_chosen_cards} with a score of {sum_score_computer}")
            black_jack()
        elif output == "draw":
            print("It's a DRAW!!!")
            print(f"    Your final hand: {user_chosen_cards} with a score of {sum_score_user}")
            print(f"    Computer's final hand: {computer_chosen_cards} with a score of {sum_score_computer}")
            black_jack()
        elif output == "blackjack_user":
            print("BLACKJACK!!!")
            print("You win!")
            print(f"    Your final hand: {user_chosen_cards} with a score of {sum_score_user}")
            print(f"    Computer's final hand: {computer_chosen_cards} with a score of {sum_score_computer}")
            black_jack()
        elif output == "blackjack_pc":
            print("The computer has a BLACKJACK.")
            print("You lose")
            print(f"    Your final hand {user_chosen_cards} with a score of {sum_score_user}")
            print(f"    Computer's final hand: {computer_chosen_cards} with a score of {sum_score_computer}")
            black_jack()
    else:
        print("Mayonnaise on an escalator, it's going upstairs so see ya later BYE BYE.")
        exit()


black_jack()

# This is definitely clean code, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# I'm sorry Uncle Bob
