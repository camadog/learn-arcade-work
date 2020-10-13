"""
quit = 'n'
while quit == 'n' or quit == 'no':
    quit = input("Do you want to quit? ")
    quit = quit.lower()
"""
"""
done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True
"""
"""
done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    if not done:
        attack = input("Does your elf attack the dragon? ")
        if attack == "y":
            print("Bad choice, you died.")
            done = True

    if not done:
        attack = input("Does your elf attempt to steal the gold? ")
        if attack == "y":
            print("Bad choice, you died.")
            done = True
"""
"""
while True: # Loop forever
    quit = input("Do you want to quit? ")
    if quit == "y":
        break

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        break

    attack = input("Does your elf attempt to steal the gold? ")
    if attack == "y":
        print("Bad choice, you died.")
        break
"""
# Review questions

print("Question 1")

i = 0
while i < 10:
    print(i)
    i += 1

print("Question 2")
print("Prediction, 2**0,2**1 ... 2**32")
print("Cause... the condition and the increment ... ")
i = 1
while i <= 2**32:
    print(i)
    i *= 2


print("Question 3")

quit = 'y'
while quit != 'no':
    quit = input("Keep looping? ")
    quit = quit.lower()

print("Question 4")

i = 10
while i >= 0:
    print(i)
    i -= 1

print("Question 5")

i = 1
while i < 10:
    print(i)
    i += 1
