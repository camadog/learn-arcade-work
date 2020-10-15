print("Problem 1")
for i in range(10):
    print("*", end=" ")
print("\n")

print("Problem 2")
for i in range(35):
    print("*", end=" ")
    if i == 9 or i == 14:
        print("\n")
print("\n")

print("Problem 3")
for i in range(10):
    for j in range(10):
        print("*", end=" ")
    print("\n")

print("Problem 4")
for i in range(10):
    for j in range(5):
        print("*", end=" ")
    print("\n")

print("Problem 5")
for i in range(5):
    for j in range(20):
        print("*", end=" ")
    print("\n")

print("Problem 6")
for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print("\n")

print("Problem 7")
for i in range(10):
    for j in range(10):
        print(i, end=" ")
    print("\n")

print("Problem 8")
for i in range(10):
    for j in range(i + 1):
        print(j, end=" ")
    print("\n")

print("Problem 9")
for i in range(10):
    k = 0
    for j in range(10 - i, 0, -1):
        print(k, end=" ")
        k += 1
    print("\n")
    for j in range(i + 1):
        print("  ", end="")
print("\n")

print("Problem 10")
for i in range(1, 10):
    for j in range(1, 10):
        n = j * i
        if n < 10:
            print(" ", end="")
        print(n, end=" ")
    print("\n")

print("Problem 11")
for i in range(1, 10):
    for j in range(10, i, -1):
        print("  ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print("\n")

#No more please :(
print("Problem 12")
for i in range(1, 10):
    for j in range(10, i, -1):
        print("  ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print("\n")
for i in range(10):
    k = 1
    print("    ", end = "")
    for j in range(8 - i, 0, -1):
        print(k, end=" ")
        k += 1
    print("\n")
    for j in range(i + 1):
        print("  ", end="")
print("\n")
#Whatever...
print("Problem 12")
for i in range(1, 10):
    for j in range(10, i, -1):
        print("  ", end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print("\n")
for i in range(8):
    k = 1
    print("    ", end = "")
    for j in range(8 - i, 1, -1):
        print(k, end=" ")
        k += 1
    for j in range(k, 0, -1):
        print(j, end=" ")
    print("\n")
    for j in range(i + 1):
        print("  ", end="")
print("\n")
