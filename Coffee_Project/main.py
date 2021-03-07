from collections import Counter
from art import coffee_art, coffee_logo

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
    "money": 0
}

penny = 0.01
nickle = 0.05
dime = 0.10
quarter = 0.25
should_continue = True

print(coffee_logo)
print("/"*70)


def coffee(coffee_choice, m_resources):
    menu_target = MENU[coffee_choice]['ingredients']
    resources_low = False
    for res in menu_target:
        for ing in m_resources:
            if (res == ing) and (m_resources[ing] < menu_target[res]):
                resources_low = True
                continue

    if resources_low:
        print("We are low on Resources!")
        return False
    else:
        print("Enter Coins:")
        quarters = int(input("Enter Quarters: "))
        dimes = int(input("Enter Dimes: "))
        nickles = int(input("Enter Nickles: "))
        pennies = int(input("Enter Pennies: "))
        payment = quarters * quarter + dimes * dime + nickles * nickle + pennies * penny
        print(f"You paid: ${round(payment, 2)}")
        change = payment - MENU[coffee_choice]['cost']
        if payment < MENU[coffee_choice]['cost']:
            print(f"Sorry that's not enough money. Money refunded: ${round(payment, 2)}")
            return False
        else:
            print(f"This is the change: ${round(change, 2)}")
            profit = payment - change
            m_resources['money'] += profit
            print(f"Enjoy you {coffee_choice} Coffee!")
            print(coffee_art)


def user_choices(choice):
    if choice == 'report':
        print(f"The resources are {resources}")
        return True
    elif choice == 'off':
        return False


while should_continue:
    user_choice = input("What would you like?\nespresso, latte, cappuccino: ").lower()
    if (user_choice == "off") or (user_choice == 'report'):
        should_continue = user_choices(user_choice)
        continue
    else:
        coffee_continue = coffee(user_choice, resources)
        if not coffee_continue:
            continue
        else:
            resources = (Counter(resources) - Counter(MENU[user_choice]['ingredients']))
