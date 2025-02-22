from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# print a report for all the current resource
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on: 
    options = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
