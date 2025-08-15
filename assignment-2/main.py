import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes here
    c = sandwich_maker_instance
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
            coins = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins, recipes[sandwich_size]["cost"]):
                c.make_sandwich(sandwich_size, recipes[sandwich_size]["ingredients"])
            


if __name__=="__main__":
    main()
