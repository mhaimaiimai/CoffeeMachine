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

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickle": 0.05,
    "pennie": 0.01
}

income = 0

def print_report():
    for item in resources:
        if item == "coffee":
            unit = "g"
        else:
            unit = "ml"
        print(f"{item.title()}: {resources[item]}{unit}")
    print(f"Money: ${income:.2f}")
    
def check_resources(coffee):
    """return 1 if resources are sufficient. otherwise, return 0"""
    for item in resources:
        if item in MENU[coffee]["ingredients"]:
            if resources[item] < MENU[coffee]["ingredients"][item]:
                return 0
    return 1              

def coin_process():
    """return total amount of money being inserted"""
    total_money = 0
    print("Please inser coins.")
    for coin in coins:
        coin_amount = int(input(f"how many {coin}s?: "))
        total_money += coin_amount*coins[coin]
    return total_money
        
def transaction_process(coffee, money):
    cost = MENU[coffee]["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refundded.")
        return False
    elif money > cost:
        print(f"Here is ${(money-cost):.2f} dollars in change.")
    
    global income
    income += (money-cost)
    return True

def update_resources(coffee):
    for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]

is_off = False
while(not is_off):
    
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request == "off":
        is_off = True
    elif request == "report":
        print_report()
    elif request in ["espresso", "latte", "cappuccino"]:
        check_resources(request)
        is_transaction_valid = transaction_process(request, coin_process())
        if is_transaction_valid:
            update_resources(request)
            print("Here is your {request}. Enjoy!")
    else:
        print("Invalid request, please try again.")
        