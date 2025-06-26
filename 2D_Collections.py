# 2D Lists

# # fruits =     ["apple", "orange", "banana", "coconut"]
# # vegetables = ["celery", "carrots", "potatoes"]
# # meats =      ["chicken", "fish", "turkey"]

# # groceries = [fruits, vegetables, meats]

# groceries = [["apple", "orange", "banana", "coconut"],
#              ["celery", "carrots", "potatoes"],
#              ["chicken", "fish", "turkey"]]


# # print(fruits[0])
# # print(fruits)
# # print(groceries)
# # print(groceries[1])
# # print(groceries[0][0])
# # print(groceries[1][2])
# # print(groceries[2][0])

# # for collection in groceries:
# #     print(collection)

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# 2D

# groceries = ({"apple", "orange", "banana", "coconut"},
#              {"celery", "carrots", "potatoes"},
#              {"chicken", "fish", "turkey"})

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# groceries = [{"apple", "orange", "banana", "coconut"},
#              {"celery", "carrots", "potatoes"},
#              {"chicken", "fish", "turkey"}]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


# groceries = [("apple", "orange", "banana", "coconut"),
#              ("celery", "carrots", "potatoes"),
#              ("chicken", "fish", "turkey")]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()


groceries = (("apple", "orange", "banana", "coconut"),
             ("celery", "carrots", "potatoes"),
             ("chicken", "fish", "turkey"))

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()













