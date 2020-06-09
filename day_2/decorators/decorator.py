# def say_hello():
#     return "Hello there!"
#
# hi = say_hello
#
# def function_caller(callback):
#     return callback()
#
# print(function_caller(hi))

# def outer_function():
#     def inner_function():
#         return "Hello from the inner function"
#
#     return (inner_function())
#
# print(outer_function)

# def make_pretty(callback):
#     def wrapper():
#         print("I am a decorated function")
#         callback()
#
#     return wrapper
#
# def do_twice(callback):
#     def wrapper():
#         callback()
#         callback()
#     return wrapper
#
# @do_twice
# def ordinary():
#     print("I am an ordinary function")
#
# ordinary()

import time

def timing_function(callback):
    def wrapper():
        time1 = time.time()
        callback()
        time2 = time.time()
        return "Time it took to run: " + str((time2 - time1))
    return wrapper

@timing_function
def my_function():
    num_list = []
    for number in range(0, 10000):
        num_list.append(number)
    print("\n Sum of all the numbers: " + str((sum(num_list))))

print(my_function())
