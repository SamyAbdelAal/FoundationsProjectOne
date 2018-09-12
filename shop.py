import re
####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################

cupcake_shop_name = "Cake'n'Cups" #complete me!
signature_flavors = ["yellow bananza","squwanch","charlie brownies"] #complete me!
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    # your code goes here!
    print("Our menu:")
    print("*******************")
    for k, v in menu.items():
        print(k, ": ", v)
    print("*******************\n")


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    # your code goes here!
    print("*******************")
    print(*original_flavors, sep=" \n")
    print("*******************\n")


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    print("*******************")
    print( *signature_flavors, sep=" \n")
    print("*******************\n")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in original_flavors or order in signature_flavors:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    ordr=input("What would you like to order? Type the name of the item exactly\n"
               "(You can add numbers at the start to order as many of the same item eg: '3 vanilla')\n"
               " or 'remove' to remove an item or "
               "'exit' to end your order: \n")\
        .lower().strip()
    # your code goes here!
    while ordr != "exit":
        if ordr == "remove":
            remove_order(order_list)
        elif has_numbers(ordr):
            num_of_order= int(re.findall(r'\d+', ordr)[0])
            ordr = ''.join([i for i in ordr if not i.isdigit()]).strip()
            if is_valid_order(ordr):
                print(num_of_order,ordr,"orders added")
                for i in range(num_of_order):
                    order_list.append(ordr)
            else:
                print("\n", ordr, "not in the menu or was misspelled\n")
        elif is_valid_order(ordr):
            print(ordr,"Added")
            order_list.append(ordr)
        else:
            print("\n", ordr,"not in the menu or was misspelled\n")

        ordr = input("Would you like to add or 'remove' another item or 'Exit' ?").lower().strip()
    return order_list


def has_numbers(string):
    return bool(re.search(r'\d', string))


def remove_order(order_list):
    """
    Repeatedly ask customer for what order to remove until they end their order by typing "Exit".
    """
    if len(order_list) !=0:
        print(*order_list, sep="\n")
        ordr = input("What would you like to remove from the order? \n"
                     "(You can add numbers at the start to order as many of the same item eg: '3 vanilla')\n"
                     "Type the name of the item exactly or 'exit' to go back: \n") \
            .lower().strip()
        # your code goes here!
        while ordr != "exit":
            if has_numbers(ordr):
                num_of_order = int(re.findall(r'\d+', ordr)[0])
                ordr = ''.join([i for i in ordr if not i.isdigit()]).strip()
                if is_valid_order(ordr):
                    print(num_of_order, ordr, "orders removed")
                    for i in range(num_of_order):
                        order_list.remove(ordr)
                else:
                    print("\n", ordr, "not in the order or was misspelled\n")
            elif is_valid_order(ordr):
                order_list.remove(ordr)
            else:
                print("\n", ordr, "not in the order or was misspelled\n")
            ordr = input("Would you like to 'remove' another item or 'Exit' to go back?").lower().strip()
    else:
        print("Sorry you haven't ordered anything yet.")
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total<5:
        print("Sorry, your order is less than 5 KD and is not eligible for credit card payment")
    else:
        print("Your order is eligible for credit card payment.")


def discount(total):
    """
    Return the total price discounted if above 7 KD.
    """
    # your code goes here!
    if total<=7:
        print("Sorry, your order is less than 7 KD and is not eligible for the discount")
    else:
        print("Your order is eligible for a 25% discount!")
        print("Your new total is:%.2f"%(total - (total*0.25)))


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for i in order_list:
        if i in menu:
            total+= menu[i]
        elif i in original_flavors:
            total+= original_price
        elif i in signature_flavors:
            total+= signature_price

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    if len(order_list) != 0:
        print("Your order is: ")
        # your code goes here!
        print(*order_list, sep=" \n")
        print("Your total is: ", get_total_price(order_list))
        discount(get_total_price(order_list))
        accept_credit_card(get_total_price(order_list))
        print("Thank you for shopping with", cupcake_shop_name)
    else:
        print("You haven't ordered anything but thanks for visiting",cupcake_shop_name)
