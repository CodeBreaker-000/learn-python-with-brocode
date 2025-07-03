# Arbitrary Arguments = Varing Arguments
# *args = Allows you to pass multiple non-key arguments(tuple)
# **kwargs = Allows you to pass multiple keyword-arguments(dictionary)
# * = unpacking operator


# def add(a, b):
#     return a+b

# print(add(1, 2))

# def add(*args):
#     # print(type(args))
#     total = 0
#     for arg in args:
#         total += arg
        
#     return total

# # add(1, 2, 3)
# # print(add(1, 2, 3, 4, 5))
# print(add(1))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
        
# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

def print_address(**kwargs):
    # print(type(kwargs))
    
    # for value in kwargs.values():
    #     print(value)
    
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street="123 Fake st",
              apt="100",
              city="Detroit", 
              state="MI", 
              zip="54321")














