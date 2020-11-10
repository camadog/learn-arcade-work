file = open("super_villains.txt")

names = []

for line in file:
    line = line.strip()
    # print(line)
    names.append(line)

file.close()

# print(names)

i = 0
while i < len(names) and names[i] != "Vidar the Manic":
    i += 1

if i == len(names):
    print("The name was not in the list.")
else:
    print("The name is at position",i)
