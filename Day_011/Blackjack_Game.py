from art import logo
import random

cards = [1,2,3,4,5,6,7,8,9,10]

continue_game = True

choice_user_card = random.choices(cards,k=2)
choice_computer_card = random.choices(cards,k=1)

while continue_game:
    Play_a_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if Play_a_game in ("y","Y","Yes","yes"):
        print(logo)
        print(f"Your card: {choice_user_card}, current score: {sum(choice_user_card)}")
        print(f"Computer's first card: {choice_computer_card[0]}")
        New_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if New_card in ("y","Y","Yes","yes"):
            choice_user_card.append(random.choice(cards))
            choice_computer_card.append(random.choice(cards))
            print(f"your final hand: {choice_user_card}, current score: {sum(choice_user_card)}")
            print(f"Computer's final hand: {choice_computer_card}, current score: {sum(choice_computer_card)}")
            if 21 < (sum(choice_user_card)) or (sum(choice_computer_card) > sum(choice_user_card)):
                print("You went over. you lose")
                continue
            else:
                print("You win")
                continue
        elif New_card in ("n","N","no","No"):
            print(f"your final hand: {choice_user_card}, current score: {sum(choice_user_card)}")
            print(f"Computer's final hand: {choice_computer_card}, current score: {sum(choice_computer_card)}")
            if 21 < (sum(choice_user_card)) or (sum(choice_computer_card) > sum(choice_user_card)):
                print("You went over. you lose")
                continue
            else:
                print("You win")
                continue
    elif Play_a_game in ("n","N","no","No"):
        print("게임을 종료합니다.")
        break
    else:
        print("잘못 입력하셨습니다.")
        print("다시 입력해주세요.")
        continue