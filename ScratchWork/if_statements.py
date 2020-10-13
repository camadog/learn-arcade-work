# Variables used in the example ''if'' statemests
a = 5
b = 4
c = 2

# Basic comparisons
if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")
if a == b:
    print("a is equal to b")
if a != b:
    print("a and b are not equal b")
if a < b and a < c:
    print("a is less than b and c")
if a < b or a < c:
    print("a is less than b or c")

a = True
if a:
    print("a is true")

a = False
if not a:
    print("a is not true")

b = False
if not a and not b:
    print("a and b are both not true")

# input function
temp = input("Whats the temperature in Celcius? ")
print("You said the temperature was " + temp + ".")

temp = input("Whats the temperature in Celcius? ")
temp = int(temp)

if temp > 50:
    print("Oh man, you could fry eggs on the pavement!")
elif temp > 35:
    print("It's hot outside.")
elif temp < 10:
    print ("It is cold outside.")
else:
    print("It is not hot outside.")

username = input("What is your name? ")
# Error statement (It's always true... cause the or comparison with "Mary" that is not cero/false):
# if username == "Paul" or "Mary":
# Correct statement:
# if username == "Paul" or username == "Mary":
# To lowercase...
if username.lower() == "paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")

print("Done")
