class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0

    def bark(self):
        """
        The first parameter of any method in a class must be self.
        This parameter is required even if the function does not use it.
        """
        print("Woof says", self.name)


# Review I guess
class Star():
    def __init__(self):
        print("A star is born!")
# 1
class Cat():
    def __init__(self):
        self.color = ""
        self.name = ""
        self.weight = 0
        
    def meow(self):
        print("meow")

# 3
class Monster():
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def decrease_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print("dead")


def main():
    # 2
    my_cat = Cat()
    my_cat.name = "Spot"
    my_cat.weight = 20
    my_cat.color = "black"
    my_cat.meow()


main()
