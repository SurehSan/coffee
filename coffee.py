MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    "money": 0,

}

def use_resources(pick):
    resources['water'] -= pick["ingredients"]["water"]
    resources['milk'] -= pick["ingredients"]["milk"]
    resources['coffee'] -= pick["ingredients"]["coffee"]

def process_coins(pick):
    print(f"A {choice} costs ${pick['cost']:.2f}.")
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f"Balance is now ${total:.2f}.")
    resources['money'] = total
    if resources['money'] < pick["cost"]:
        print("Sorry, not enough coins.")
    else:
        change = resources['money'] - pick["cost"]
        resources['money'] = change
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {choice}, enjoy!")
        use_resources(pick)

def check_resources(pick, resources):
    if resources["water"] < pick["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
    elif pick == "espresso":
        if resources["milk"] < pick["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
    elif resources["coffee"] < pick["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        process_coins(pick)

coffee_on = True
while coffee_on:
    choice = input("What would you like next? (espresso/latte/cappuccino/report/off): ")
    if choice == "off":
        coffee_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${resources['money']:.2f}")
    elif choice == "espresso":
            check_resources(MENU["espresso"], resources)
    elif choice == "latte":
        check_resources(MENU["latte"], resources)
    elif choice == "cappuccino":
        check_resources(MENU["cappuccino"], resources)
    else:
        print("Invalid response.")
