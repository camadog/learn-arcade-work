# Variables and expressions

answer = "bananas"
print(answer)

print("The answer is", answer, ".")

print("The answer is " + answer + ".")

answer = 42
# Error:
# print("The answer is " + answer + ".")
print("The answer is " + str(answer) + ".")
# *** formated string ***
print(f"The answer is {answer}.")
