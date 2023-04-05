# Setting

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
}

money = 0

# def

def report():
    print(f"""
    Water: {resources["water"]}
    Milk: {resources["milk"]}
    Coffee: {resources["coffee"]}
    Money: ${money}
    """)
def money_check(coffee):
    global resources
    global money
    # 돈 체크 
    if MENU[coffee]["cost"] < total_coin:
        if coffee == "espresso":
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            money += MENU[coffee]["cost"]
        else:
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            money += MENU[coffee]["cost"]          
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def resources_check(coffee):
    # 자원 체크 
    global resources
    global money
    if coffee == "espresso":
        if (resources["water"] - MENU[coffee]["ingredients"]["water"]) < 0:
            print("Sorry there is not enough water")
            return False
        elif (resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]) < 0:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
    else:
        if (resources["water"] - MENU[coffee]["ingredients"]["water"]) < 0:
            print("Sorry there is not enough water")
            return False
        elif (resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]) < 0:
            print("Sorry there is not enough coffee")
            return False
        elif (resources["milk"] - MENU[coffee]["ingredients"]["milk"]) < 0:
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    




def order_coffee(coffee):
    global total_coin
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) 
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total_coin = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    print(total_coin)
    if money_check(coffee):
        refune = round((total_coin - MENU[coffee]["cost"]),1)
        print(f"Here is ${refune} in change.")
        print(f"Here is your {coffee}. Enjoy!")

# main
while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "espresso":
        if resources_check(coffee = order):
            order_coffee("espresso")
    elif order == "latte":
        if resources_check(coffee = order):
            order_coffee("latte")
    elif order == "cappuccino":
        if resources_check(coffee = order):
            order_coffee("cappuccino")
    elif order == "fill":
        resources["water"] += 300
        resources["coffee"] += 200
        resources["milk"] += 100
    elif order == "report":
        report()
    elif order == "off":
        break
    else:
        print("잘못 입력하셨습니다.")
        continue
    