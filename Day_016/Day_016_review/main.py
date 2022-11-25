from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_item = menu.get_items()
coffemaker = CoffeeMaker()
monymachine = MoneyMachine()
is_on = True

while is_on:
    order_drink = input(f"What would you like? ({menu_item}): ")
    if order_drink == "off":
        is_on = False
    elif order_drink == "report":
        coffemaker.report()
        monymachine.report()
    else:
        drink = menu.find_drink(order_drink)
        if coffemaker.is_resource_sufficient(drink):
            cost = drink.cost
            monymachine.make_payment(cost)
            coffemaker.make_coffee(drink)