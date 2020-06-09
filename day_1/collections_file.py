my_list = ["spam", "ham", "eggs"]

print(my_list[0])

numbers = [1,2,3,4,5,6,7,8,9]

print(sum(numbers))

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]

stops.insert(0, "Queen Street")

print(stops)

print(stops.index("Croy"))

stops.insert(4, "Polmont")

print(stops)


stops.remove("Haymarket")

print(stops)

# Python 3
stops.clear()

# Python 2
del stops[:]

print(stops)


# Tuples
# person = ("Frank", 37, "Bacon Enthusiast", True)

# print(person)

# print(len(person))


# NamedTuples

from collections import namedtuple

Person = namedtuple("Person", "name age job")

person = Person("George", 37, "Bacon Enthusiast")

print(person)

user = {"name": "Christine", "age": 40}

user["email"] = "egg@bacon.com"

print(user)