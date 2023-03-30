from art import logo
import random

# card
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#카드 뽑기 함수
def draw_card(count):
    for i in range(count):
        my_card.append(random.choice(cards))
        if add_computercard() < 21:
            computer_card.append(random.choice(cards))
        elif add_computercard() > 21 and (11 in computer_card):
            computer_card.remove(11)
            computer_card.append(1)
            computer_card.append(random.choice(cards))
        else:
            pass



# 점수 계산 함수

def add_mycard():
    my_card_score = 0
    for i in range(len(my_card)):
        my_card_score += my_card[i]
    return my_card_score



def add_computercard():
    computer_card_score = 0
    for i in range(len(computer_card)):
       computer_card_score += computer_card[i]
    return computer_card_score

# 결과 계산 함수

def result_game():
    print(f"""
    your final hand: {my_card}, final score: {add_mycard()}
    Computer's final hand: {computer_card}, final score: {add_computercard()}
    """)
    if add_mycard() > 21:
        print("you lose 😤\n")
    elif add_computercard() > 21 or add_mycard() == 21: 
        print("You win!!!!\n")
    elif add_mycard() == 21 and add_computercard() == 21:
        print("draw")
    elif add_mycard() > add_computercard():
        print("You win!!!!\n")
    else:
        print("you lose 😤\n")

# 진행 여부
def continue_game():
    while True:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            draw_card(1)
            print(f"Your card: {my_card}, current score: {add_mycard()}")
            print(f"Computer's first card: {computer_card[0]}\n")
            if add_mycard() > 21:
                result_game()
                Black_jack_game = False
                break
        else:
            result_game()
            Black_jack_game = False
            break



# Black_jack 게임
Black_jack_game = True
while Black_jack_game:
    my_card = []
    computer_card = []
    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_blackjack == "y":
        draw_card(2)
        print(logo)
        print(f"Your card: {my_card}, current score: {add_mycard()}")
        print(f"Computer's first card: {computer_card[0]}\n")
        continue_game()
    else:
        print("게임을 종료하겠습니다.")
        break