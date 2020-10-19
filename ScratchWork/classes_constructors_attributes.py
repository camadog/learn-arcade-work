"""
    Normal way:

class Address:
    def __init__(self,
        name: str = "",
        line1: str = "",
        line2: str = "",
        city: str = "",
        state: str = "",
        zip_code: str = ""
    ):
        self.name: str = name
        self.line1: str = line1
        self.line2: str = line2
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code

python3.8: @dataclass
"""
from dataclasses import dataclass
@dataclass
class Address:
    name: str = ""
    line1: str = ""
    line2: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""


class Cat:
    """Singleton  == static variable"""
    population = 0
    def __init__(self, name):
        self.name = name
        Cat.population += 1

class Character:
    """
    Comments are important
    """
    def __init__(self):
        """
        constructor == dunder method == magic method
        dunder = double under scored
        """
        """ Data type """
        self.name: str = "placeholder"
        self.outfit = ""
        self.max_hp = 0
        self.current_hp = 0
        self.armor_amount = 0
        self.max_speed = 0

def main():
    player = Character()
    print(player.name)
    player.name = "Jim"
    player2 = Character()
    player2.name = "Other"
    cat1 = Cat("Pat")
    cat2 = Cat("Pepper")
    cat3 = Cat("Pouncy")

    Cat.population = 4
    #New field
    cat2.population = 5
    print("The cat population is:",Cat.population)
    print("The cat population is:",cat1.population)
    print("The cat population is:",cat2.population)
    print("The cat population is:",cat3.population)

    address = Address("name","l1","l2","city","state","zip")
    print(address)

main()
