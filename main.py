### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources.get(item, 0):
                print(f"Sorry there is not enough res.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        total = 0
        total += int(input("how many dollars?: ")) * 1
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.1

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"${sandwich_size} Sandwich is ready. Bon appetit!")


c = SandwichMachine(resources)
while True:
    
    sandwich_size = input("What would you like? (small/medium/large/off/report): ")

    if sandwich_size == "report":
        print(f"Bread: {c.machine_resources['bread']} slices")
        print(f"Ham: {c.machine_resources['ham']} slices")
        print(f"Cheese: {c.machine_resources['cheese']} ounces")

    elif sandwich_size == "off":
        break

    
    else:
        
        print("Please insert coins.")
        coins = c.process_coins()
        if c.transaction_result(coins, recipes[sandwich_size]["cost"]):
            c.make_sandwich(sandwich_size, recipes[sandwich_size]["ingredients"])
        




### Make an instance of SandwichMachine class and write the rest of the codes ###