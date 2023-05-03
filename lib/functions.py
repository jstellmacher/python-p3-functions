#!/usr/bin/env python3

def greet_programmer():
    print(f"Hello, programmer!")
# greet_programmer()

def greet(Naureen):
    print(f"Hello, {Naureen}!")
# greet()


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
# greet_with_default()

def add(num1, num2):
    return num1+num2
# add()

# def halve(number):
#     if type {number} != "number"
#         return null;
#     return number/2;
# halve()
def halve(number):
    if type (number) == int:
        return number / 2
    elif type(number) == float:
        return number / 2.0 
    else:
        return None