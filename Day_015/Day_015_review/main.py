MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

def calculate_coin():
    """전체 코인 계산 함수"""
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    pennie = int(input("how many pennies?: "))

    coins = (quarter * 0.25 + dime * 0.10 + nickle * 0.05 + pennie * 0.01)
    change = coins - MENU[choice]["cost"]
    print(f"Here is ${change} in change.")
    print(f"Here is your {choice}")

def alter_resource():
    """자원 부족 시 알림"""
    if resources["water"] < 0 :
        print("Sorry ther is not enough water.")
    elif resources ["milk"] < 0 :
        print("Sorry ther is not enough milk.")
    elif resources ["coffee"] < 0 :
        print("Sorry ther is not enough coffee.")

def choice_coffee():
    CoffeeMachine_on = True
    while CoffeeMachine_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "latte":
            resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resources["money"] + MENU["latte"]["cost"]
            alter_resource()
        elif choice == "espresso":
            resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            resources["money"] + MENU["espresso"]["cost"]
            alter_resource()
        elif choice == "cappuccino":
            resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resources["money"] + MENU["cappuccino"]["cost"]
            alter_resource()
        elif choice == "report":
            print(f"""
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${resources["money"]}
            """)
            continue
        elif choice == "off":
            CoffeeMachine_on = False
        else:
            print("잘못입력했습니다 다시 입력해주세요")
            continue
        print("Please insert coins.")
        quarter = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickle = int(input("how many nickles?: "))
        pennie = int(input("how many pennies?: "))

        coins = (quarter * 0.25 + dime * 0.10 + nickle * 0.05 + pennie * 0.01)
        change = round(coins - MENU[choice]["cost"],1)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}")
        

# # 거스름돈 계산 및 커피 내어주기
# def change_coin():
#     change = coins - resources["money"]
#     print(f"Here is ${change} in change.")
#     print(f"Here is your {choice}")

# CoffeeMachine Main 
# CoffeeMachine_on = True
# while CoffeeMachine_on:
#     choice_coffee()
#     calculate_coin()
#     change_coin(coins, choice, resources)

choice_coffee()