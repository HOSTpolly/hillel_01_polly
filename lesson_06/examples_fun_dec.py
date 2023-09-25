# Functions


from decorators import do_twice
from decorators import timer


def add_one(number):
    return number + 1


# print (add_one(2))
# In Python, functions are first-class objects.
# This means that functions can be passed around and used as arguments,
# just like any other object (string, int, float, list, and so on).
# Consider the following three functions:


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))
print(greet_bob(be_awesome))


# It’s possible to define functions inside other functions.
# Such functions are called inner functions.
# Here’s an example of a function with two inner functions:

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# print(parent())


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"
    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)
print(first())
print(second())


# внутрішні функції в межах батьківської функції
# print(first)
# print(second)
# посилання на кожну функцію, яку  можna викликати в майбутньому

# Прості декоратори


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_whee():
    print("Whee!")
# По суті, назва say_whee тепер вказує на wrapper()-внутрішню функцію.
# повертає wrapper як функцію, коли викликає my_decorator(say_whee):


say_whee = my_decorator(say_whee)
print(say_whee())


# Однак wrapper()має посилання на оригінал say_whee()як func,
# і викликає цю функцію між двома викликами print().

# !!!!!!декоратори обертають функцію, змінюючи її поведінку!!!!!!!
# Оскільки wrapper()це звичайна функція Python,
# спосіб модифікації декоратором функції може динамічно змінюватися.

# from datetime import datetime

# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = not_during_the_night(say_whee)

# print(say_whee)


def my_decorator_1(func):
    def wrapper_1():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper_1


@my_decorator_1
def say_whee():
    print("Whee!")


@do_twice
def say_whee():
    print("Whee!")


print(say_whee())


@do_twice
def greet(name):
    print(f"Hello, {name}")


print(greet("World"))


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)

# say_whee.__name__
# help(say_whee)


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


print(waste_some_time(1))
print(waste_some_time(999))
