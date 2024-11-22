from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
# latte = MenuItem()
# espresso = MenuItem()
# cappuccino = MenuItem()

is_on = True

# money_report = money_machine.report()
# pay = money_machine.make_payment(2)

# latte.name = "latte"
# latte.ingredients.water = 200
# latte.ingredients.milk = 150
# latte.ingredients.coffee = 24
# latte.cost = 2.5

# espresso.name = "espresso"
# espresso.water = 50
# espresso.milk = 0
# espresso.coffee = 18
# espresso.cost = 1.5

# cappuccino.name = "cappuccino"
# cappuccino.water = 250
# cappuccino.milk = 50
# cappuccino.coffee = 24
# cappuccino.cost = 3

# print(latte.name)

def turn_off():
  global is_on
  print("Turning off... Goodbye. 😴")
  is_on = False
def order():
  return True

def prompt():
  user_input = input("What would you like? (espresso/latte/cappuccino) ☕: ")
  if user_input == MenuItem():
    order()
  elif user_input == "report":
    money_machine.report()
  elif user_input == "off":
    turn_off()

while is_on == True:
  prompt()