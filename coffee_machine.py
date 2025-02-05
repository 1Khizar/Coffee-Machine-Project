print("COFFEE MACHINE")

# Dictionary for storing the ingredients of the drinks available
ingredients={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}

profit=0

# Resources in the Coffe Machine available
resources={
    "water":600,
    "milk":500,
    "coffee":100,
}

# Function for checking the resources available in the machine for the drink order by user
def checkresources(drink_order):
  for item in drink_order:
    if drink_order[item] >= resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

# Taking money from the user
def processcoin():
  print("Please insert coins.")
  quarters=int(input("How many quarters?:"))
  dimes=int(input("How many dimes?:"))
  nickles=int(input("How many nickles?:"))
  pennies=int(input("How many pennies?:"))
  total_user_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

  return total_user_money

# Checking the money entered by the user is enough for the drink cost
def transaction_successful(money_received,drink_cost):
  if money_received >= drink_cost:
    change=round(money_received-drink_cost,2)
    print(f"Here is ${change} in change.")
    global profit
    profit+=drink_cost
    return True
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False

def make_coffee(drink_name, drink_ingredients):
  for item in drink_ingredients:
    resources[item] -= drink_ingredients[item]
  print(f"Enjoy your coffee {drink_name}☕☕☕")


# Start
machine_is_ON=True

while machine_is_ON:
  choice=input("What would you like? (espresso/latte/cappuccino):")

  if choice=="off":
      machine_is_ON=False

  elif choice=="report":
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {profit}$")

  else:
    print(choice)

    checkresources(ingredients[choice]["ingredients"])
    payment=processcoin()
    if transaction_successful(payment, ingredients[choice]['cost']):
      make_coffee(choice, ingredients[choice]["ingredients"])
