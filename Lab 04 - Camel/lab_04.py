import random

def print_instructions():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.")
    print()

def main():
    done = False

    thirst = 0
    canteen = 3
    traveled_miles = 0
    camel_tiredness = 0
    user_choice = ' '

    distance = 20
    natives_distance = -20

    print_instructions()

    while not done:
        # Ask
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")
        user_choice = user_choice.upper()
        print()

        # Do
        if user_choice == 'Q':
            done = True
            break

        elif user_choice == 'E':
            print("Miles traveled:", traveled_miles)
            print("Drinks in canteen:", canteen)
            print("The natives are", distance,  "miles behind you.")

        elif user_choice == 'D':
            camel_tiredness = 0
            natives_distance += random.randrange(7, 14);
            print("The camel is happy.")

        elif user_choice == 'C' or user_choice == 'B':
            if user_choice == 'C':
                camel_tiredness += random.randrange(1, 3)
                miles = random.randrange(10, 20)
            elif user_choice == 'B':
                camel_tiredness += 1
                miles = random.randrange(5, 12)

            thirst += 1
            traveled_miles += miles
            natives_distance += random.randrange(7, 14);
            oasis = random.randrange(21)

            if oasis == 7:
                thirst = 0
                canteen = 3
                camel_tiredness = 0
                print("*You have found an oasis, now your canteen is full.")

            print("You have traveled", miles, "miles.")

        elif user_choice == 'A':
            if canteen > 0:
                thirst = 0
                canteen -= 1
            else:
                print("*There is no more water left in the canteen!")

        # Calculate new distance
        distance = (natives_distance - traveled_miles) * -1

        # Game enders
        if distance <= 0:
            print("The natives have caught you up.")
            done = True
            break
        if camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
            break
        if thirst > 6:
            print("You died of thirst!")
            done = True
            break
        if traveled_miles >= 200:
            print("You made it across the desert! You won!")
            done = True
            break

        # User notify
        if distance > 0  and distance < 15:
            print("The natives are getting close!")
        if thirst > 4:
            print("You are thirsty!")
        if camel_tiredness > 5:
            print("Your camel is getting tired.")

        print()

    print("Game over.")
    print()

main()
