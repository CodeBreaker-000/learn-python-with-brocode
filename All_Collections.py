# Collection  = Single variable used to store multiple values
# List = [] ordered and changeable. Duplicates OK.
# Set  = {} unordered and immutable, but Add/Remove OK. No duplicates
#Tuple = () ordered and unchangeable. Duplicates OK. Faster


# List

# fruits = ["Apple", "Orange", "Banana", "Coconut"]

# # print(fruits)
# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])
# # print(fruits[3])
# # print(fruits[:3])
# # print(fruits[::2])
# # print(fruits[::-1])

# # for fruit in fruits:
# #     print(fruit)

# # print(dir(fruits))     # shows all the methods a list can perform
# # print(help(fruits))

# # print(len(fruits))
# # print("Apple" in fruits)
# # print("Pineapple" in fruits)

# # fruits[0] = "Pineapple"
# # for fruit in fruits:
# #     print(fruit)

# # fruits.append("Pineapple")
# # print(fruits)
# # fruits.remove("Apple")
# # print(fruits)
# # fruits.insert(0, "Pineapple")
# # print(fruits)
# # fruits.sort()
# # print(fruits)
# # fruits.reverse()
# # print(fruits)
# # fruits.sort()
# # fruits.reverse()
# # print(fruits)
# # fruits.clear()
# # print(fruits)
# # print(fruits.index("Apple"))
# # print(fruits.count("Banana"))
# print(fruits.count("Pineapple"))


# Set

# fruits = {"Apple", "Orange", "Banana", "Coconut", "Coconut"}

# # print(fruits)
# # print(dir(fruits))     # shows all the methods a list can perform
# # print(help(fruits))

# # for fruit in fruits:
# #     print(fruit)

# # print(len(fruits))
# # print("Apple" in fruits)
# # print("Pineapple" in fruits)

# # fruits.add("Pineapple")
# # print(fruits)
# # fruits.remove("Apple")
# # print(fruits)
# # fruits.pop()     # Random element will get popped
# # print(fruits)
# fruits.clear()
# print(fruits)


# Tuple

fruits = ("Apple", "Orange", "Banana", "Coconut", "Coconut")

# print(fruits)
# print(dir(fruits))     # shows all the methods a list can perform
# print(help(fruits))

# print(len(fruits))
# print("Apple" in fruits)
# print("Pineapple" in fruits)

# for fruit in fruits:
#     print(fruit)

# print(fruits.index("Apple"))
print(fruits.count("Coconut"))


