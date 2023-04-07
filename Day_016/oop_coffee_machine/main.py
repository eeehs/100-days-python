from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
coffee_menu = Menu()
money_checker = MoneyMachine()


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        break
    elif order == "report":
        coffee_maker.report()
        money_checker.report()
    else:
        drink = coffee_menu.find_drink(order_name=order)
        if coffee_maker.is_resource_sufficient(drink=drink):
            if money_checker.make_payment(cost=drink.cost):
                coffee_maker.make_coffee(order=drink)
