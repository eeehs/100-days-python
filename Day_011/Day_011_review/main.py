from art import logo
import random , os , time

def mycard_counting(k):
    """
    내 카드 셔플 및 제공 함수
    """
    card = random.sample(cards, k)
    for car in card:
        your_card.append(car)

    if (sum(your_card)> 21) and (11 in your_card):
        your_card[your_card.index(11)] = 1


def Computer_counting(k):
    card = random.sample(cards, k)
    for car in card:
        if sum(Computer_card) < 18:
            Computer_card.append(car)
        else:
            pass
    if (sum(Computer_card)> 21) and (11 in Computer_card):
        Computer_card[Computer_card.index(11)] = 1
    

def calculate_score():
    global i
    if sum(your_card) > 21:
        os.system('cls')
        print("#########################게임이 종료되었습니다#########################")
        print(f"your final hand: {your_card},final score: {sum(your_card)}")
        print(f"Computer's final hand: {Computer_card}, final score: {sum(Computer_card)}")
        print("당신이 졌습니다.")
        print("#####################################################################")
        i = i + 1 
    elif sum(your_card) == 21:
        os.system('cls')
        print("#########################게임이 종료되었습니다#########################")
        print("#############21점을 맞춰서 블랙잭으로 당신이 이겼습니다#################")
        print("#####################################################################")
        i = i + 1 
    else:
        pass
def final_calculate():
    
    if sum(your_card) > sum(Computer_card):
        print("당신이 이겼습니다")

    elif sum(Computer_card) > 21:
        print("당신이 이겼습니다")
    
    else: 
        print("당신이 졌습니다.")



while True:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    your_card = []
    Computer_card = []
    i = 0 

    play_blackjack = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    os.system('cls')
    if play_blackjack in ['yes','y']:
        print(logo)
        mycard_counting(2)
        Computer_counting(10)
        print(f"Your card: {your_card}, current score: {sum(your_card)}")
        print(f"Computers's first card: {Computer_card[0]}")
        calculate_score()

        while i == 0:
            continue_game = input("Type 'y' to get another card, tpye 'n' to pass: ")

            if continue_game in ['yes','y']:
                mycard_counting(1)
                Computer_counting(1)
                print(f"Your card: {your_card}, current score: {sum(your_card)}")
                print(f"Computers's first card: {Computer_card[0]}")
                calculate_score()
            else:
                os.system('cls')
                print("#########################게임이 종료되었습니다#########################")
                print("---------------------------------최종결과---------------------------------")
                print(f"Your final hand: {your_card},final score: {sum(your_card)}")
                print(f"Computer's final hand: {Computer_card}, final score: {sum(Computer_card)}")
                print("---------------------------------최종결과---------------------------------")
                final_calculate()
                break

                
    else:
        os.system('cls')
        print("게임 종료")
        break