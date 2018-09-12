from shop import (
    print_menu,
    print_originals,
    print_signatures,
    get_order,
    print_order,
    cupcake_shop_name
)

print("Welcome to",cupcake_shop_name, "You can get 25% off on all orders above 7 KD")
print_menu()
print_originals()
print_signatures()
order_list = get_order()
print_order(order_list)
input('Press ENTER KEY to close window')