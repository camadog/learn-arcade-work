#ForEach
"""
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)

#Regular for by index
my_list = [101, 20, 10, 50, 60]
for index in range(len(my_list)):
    print(my_list[index])

#Looping With Both An Index And Element
for index, value in enumerate(my_list):
    print(index, value)

#Adding to a List
my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)
my_list += [10]
print(my_list)

#Empty list
list = [0]*10
print(list)

list = []
for i in range(5):
    user_input = input("Enter something: ")
    list.append(user_input)
    print(list)

#Summing or Modifying a List
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]
list_total = 0

for index in range(len(my_list)):
    list_total += my_list[index]

print(list_total)

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop through array, copying each item in the array into
# the variable named item.
for item in my_list:
    # Add each item
    list_total += item

# Print the result
print(list_total)



# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Modify the element by doubling it
    my_list[index] = my_list[index] * 2

# Print the result
print(my_list)

#Slicing Strings

# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop through each element in myArray
for item in my_list:
    # This doubles item, but does not change the array
    # because item is a copy of a single element.
    item = item * 2

# Print the result
print(my_list)

x = "This is a sample string"
#x = "0123456789"

print("x=", x)

# Accessing the first character ("T")
print("x[0]=", x[0])

# Accessing the second character ("h")
print("x[1]=", x[1])

# Accessing from the right side ("g")
print("x[-1]=", x[-1])

# Access 0-5 ("This ")
print("x[:6]=", x[:6])
# Access 6 to the end ("is a sample string")
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

for character in "This is a test.":
    print(character)


months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
n = (n - 1) * 3
print(months[n:n+3])
"""

plain_text = "This is a test. ABC abc"

for c in plain_text:
    print(ord(c), end=" ")
print()

for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    print(c2, end="")
print()

encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    print(c2, end="")

print()

#Associative Arrays


# Create an empty associative array
# (Note the curly braces.)
x = {}

# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

# Fetch and print an item
print(x["fred"])
print(x)
