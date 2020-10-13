"""
user_guess = 0
secret_number = 20
user_attempt_number = 1

while user_guess != secret_number and user_attempt_number < 8:
    # Tell the user what attempt we are on, and get their guess:
    print("*Atempt:",user_attempt_number)
    user_input_text = input("Guess what number I am thinking of: ")
    user_guess = int(user_input_text)
    user_attempt_number += 1

    # Print if we are too high or low, or we got it.
    if user_guess > secret_number:
        print("Too high.")
    elif user_guess < secret_number:
        print("Too low.")
    else:
        print("You got it!")
    if user_attempt_number == 8:
        print("You lose! The number was:", secret_number)
"""
total = 0
for i in range(5):
    number = int(input("Enter a number: "))
    total = total + number
print("The total is: ", total)

for i in range(10):
    print(i)

for i in range(10):
    print(i+1)

for i in range(1, 11):
    print(i)

for i in range(2, 12, 2):
    print(i)

for i in range(5):
    print((i + 1) * 2)

for i in range(10, 0, -1):
    print(i)

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

for i in range(5):
    print("I will ont chew gum in class.")

# Ask
repetitions = int(input("How many times should I repeat? "))

# Loop
for i in range(repetitions):
    print("I will not chew gum in class.")

def print_about_gum(repetitions):
    for i in range(repetitions):
        print("I will not chew gum in class.")

def main():
    print("Main")
    print_about_gum(5)

main()
