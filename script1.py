# THIS IS WITH if_name_main.py FILE 


# print(dir())

# from script2 import *

# print(__name__)


def favorite_food(food):
    print(f"Your favorute food is {food}")

def main():
    print("This is script 1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()






