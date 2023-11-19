from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = True
current_score = 0
computer_score = 0

while start_game:
    print(logo)
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if want_to_play == 'y':
        start_game = True
        current_cards = [str(random.choice(cards)), str(random.choice(cards))]
        current_score = int(current_cards[0]) + int(current_cards[1])
        computer_cards = [str(random.choice(cards))]
        computer_score = int(computer_cards[0])
        print("Your cards:", current_cards, "Current Score: ", current_score)
        print("Computer's first card:", computer_score)
        if current_score == 21:
            print("Blackjack you win.")
            start_game = False
        elif computer_score == 21:
            print("Blackjack you lose.")
            start_game = False
        elif current_score != 21 and computer_score != 21:
            while True:
                pickup_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if pickup_card == "y": 
                    current_cards.append(str(random.choice(cards)))
                    current_score = sum([int(card) for card in current_cards])
                    print("Your cards:", current_cards, "Current Score: ", current_score)
                    if current_score > 21 and "11" in current_cards:
                        current_cards[current_cards.index("11")] = "1"
                        current_score = sum([int(card) for card in current_cards])
                    elif current_score > 21:
                        print("You lose.")
                        start_game = False
                        break
                elif pickup_card == "n":
                    while computer_score < 17:
                        computer_cards.append(str(random.choice(cards)))
                        computer_score = sum([int(card) for card in computer_cards])
                    print("Computer's cards:", computer_cards, "Computer's Score: ", computer_score)
                    if computer_score > 21:
                        print("You win.")
                        start_game = False
                        break
                    elif current_score > computer_score:
                        print("You win.")
                        start_game = False
                        break
                    elif current_score < computer_score:
                        print("You lose.")
                        start_game = False
                        break
                    elif current_score == computer_score:
                        print("Draw")
                        start_game = False
                       
