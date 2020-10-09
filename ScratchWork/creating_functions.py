# Creating Functions

def print_hello():
    """ Describe the function here """
    print("Hello!")
def print_goodbye():
    """ Describe the function here """
    print("Goodbye!")
#Parameters
def print_number(number):
    print(number)
def add_numbers(a, b):
    print(a + b)
"""
Don't:
def add_numers(a, b):
    # Avoid limiting functionality by creating a function that always does the same
    a = 11
    b = 7
    print(a + b)
"""
# Returning
def sum_two_numbers(a, b):
    result = a + b
    # don't use return(result)
    return result
def volume_cylinder(radious, height):
    """
    Returns volume of a cylinder given radious, height.
    :param float radious: The radious of the cylinder.
    :param float height: The height of the cylinder.
    """
    pi = 3.141592653589
    volume = pi * radious ** 2 * height
    return volume

# Scope
x = 44
def f1():
    # x will be readonly... if you try to change it will trow an error
    print(x)
# Parameters will be passed as referece / copy
def f2(x):
    x += 1
    print(x)


def main():
    # Call the functions
    print_hello()
    print_goodbye()
    print_number(55)
    print_number(25)
    print_number(8)
    add_numbers(11, 7)
    result = sum_two_numbers(22, 15)
    print(result)
    y = 10
    f2(y)
    print(y)
#Good practice
if __name__ == "__main__":
    main()
