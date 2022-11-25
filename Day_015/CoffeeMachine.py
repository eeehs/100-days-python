from main import MENU , resources

resource = {
    "Water": 300,
    "Milk" : 200,
    "Coffee" : 100,
    "Money" : 0
}

coins = {
    "quarter": 0.25,
    "dime" : 0.10,
    "nickle" : 0.05,
    "pennie" : 0.01
}

def total_coin():
    """코인이 총 얼마인지 계산하는 함수"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    
    quarters = quarters * coins["quarter"]
    dimes = dimes * coins["dime"]
    nickles = nickles * coins["nickle"]
    pennies = pennies * coins["pennie"]

    total = quarters + dimes + nickles + pennies

    return total

while True:
    Choice_Coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if Choice_Coffee == "off":
        break
    if Choice_Coffee == "report":
        print(f"""
        Water : {resource["Water"]}ml
        Milk  : {resource["Milk"]}ml
        Coffee: {resource["Coffee"]}g
        Money : ${resource["Money"]}
        """)
        continue
    if Choice_Coffee == "espresso":
        if resource["Water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            continue
        elif resource["Coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            continue
        A = total_coin()
        if A < MENU["espresso"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:    
            resource["Money"] = resource["Money"] + MENU["espresso"]["cost"]
            resource["Water"] = resource["Water"] - MENU["espresso"]["ingredients"]["water"]
            resource["Coffee"] = resource["Coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            print(f"""
            Here is ${round((A - MENU["espresso"]["cost"]),2)} in change.
            Here is your espresso. Enjoy!
            """)
        continue
    elif Choice_Coffee == "latte":
        if resource["Water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            continue
        elif resource["Coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            continue
        elif resource["Milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            continue
        A = total_coin()
        if A < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resource["Money"] = resource["Money"] + MENU["latte"]["cost"]
            resource["Water"] = resource["Water"] - MENU["latte"]["ingredients"]["water"]
            resource["Coffee"] = resource["Coffee"] - MENU["latte"]["ingredients"]["coffee"]
            resource["Milk"] = resource["Milk"] - MENU["latte"]["ingredients"]["milk"]
            print(f"""
            Here is ${round((A - MENU["latte"]["cost"]),2)} in change.
            Here is your latte. Enjoy!
            """)
        continue
    elif Choice_Coffee == "cappuccino":
        if resource["Water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            continue
        elif resource["Coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            continue
        elif resource["Milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            continue
        A = total_coin()
        if A < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:    
            resource["Money"] = resource["Money"] + MENU["cappuccino"]["cost"]
            resource["Water"] = resource["Water"] - MENU["cappuccino"]["ingredients"]["water"]
            resource["Coffee"] = resource["Coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            resource["Milk"] = resource["Milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            print(f"""
            Here is ${round((A - MENU["cappuccino"]["cost"]),2)} in change.
            Here is your cappuccino. Enjoy!
            """)
        continue
    else:
        print("잘못입력했습니다. 다시 입력해주세요")
        continue
        
