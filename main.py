from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
  options = menu.get_items()
  user_input = input(f"What would you like? ({options}) ☕: ")
  if user_input == "off":
    print("Turning off... Goodbye. 😴")
    is_on = False
  elif user_input == "report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(user_input)
    if drink:
      if coffee_maker.is_resource_sufficient(drink):
        print(f"That will be ${format(drink.cost, '.2f')}.")
        if money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)