# Variable scope = where a variable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in


# local scope

# def func1():
#     x = 1    # here x is the local variable of func1
#     print(x)

# def func2():
#     x = 2    # here x is the local variable of func2
#     print(x)

# func1()
# func2()


# Enclosed scope

# def func1():
#     x = 1    
#     def func2():
#         print(x)
#     func2()

# func1()


# Global scope

# x = 1
# def func1():
#     def func2():
#         print(x)
#     func2()
    
# func1()


# Built-in

from math import e

def fun1():
    print(e)    # e is built-in variable

fun1()



