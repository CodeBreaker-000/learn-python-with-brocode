# Default Arguments: Used when some same arguments are used repeatedly in a function.
#                    So we just fix the argument as default.   

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))























