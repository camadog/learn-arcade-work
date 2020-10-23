"""
Notes:
* Keep in mind "IS A" test-relationship for inheritance...
* Calling the partent's constructor is not forced on python
"""

# Example of an instance variable
class ClassA():
    def __init__(self):
        self.y = 3

# Example of a static variable
class ClassB():
    # only singletones ...
    x = 7


class Person():
    def __init__(self):
        self.name = ""

    def report(self):
        # Basic report
        print("Report for", self.name)

class Employee(Person):
    def __init__(self):
        # Call the parent/super class constructor first
        super().__init__()

        # Now set up our variables
        self.job_title = ""

    def report(self):
        # Here we override report and just do this:
        print("Employee report for", self.name)

class Customer(Person):
    def __init__(self):
        super().__init__()
        self.email = ""

    def report(self):
        # Run the parent report:
        super().report()
        # Now add our own stuff to the end so we do both
        print("Customer e-mail:", self.email)

def main():
    john_smith = Person()
    john_smith.name = "John Smith"

    jane_employee = Employee()
    jane_employee.name = "Jane Employee"
    jane_employee.job_title = "Web Developer"

    bob_customer = Customer()
    bob_customer.name = "Bob Customer"
    bob_customer.email = "send_me@spam.com"

    john_smith.report()
    jane_employee.report()
    bob_customer.report()

    # Create class instances
    a = ClassA()
    b = ClassB()
    c = ClassB()

    # Two ways to print the static variable.
    # The second way is the proper way to do it.
    print(b.x) # Aqui si se refiere al singleton
    print(c.x)
    print(ClassB.x)

    # Instance Variables Hiding Static Variables
    # changes de value of the singleton / static variable
    ClassB.x = 8
    # This creates a new instance variable and sets its value to 10
    b.x = 10

    print(ClassB.x)
    print(b.x)


    # One way to print an instance variable.
    # The second generates an error, because we don't know what instance
    # to reference.
    print(a.y)
    # print(ClassA.y)

main()
