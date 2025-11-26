class Person:
    """ class that represent a person """
    def __init__(self, name, age):
        """
        Args:
            name = Name of the person
            age = Age of the person
        """
        self.name = name
        self.age = age

    def display_details(self):
        """ Display details of the person"""
        print(
            f"\nName : {self.name}\n"
            f"Age : {self.age}"
            )


class Employee(Person):
    """ class that represent an Employee, inherited from the class Person"""
    def __init__(self, name, age, salary):
        """
        Args:
            name = Name of the employee
            age = Age of the employee
            salary : Salary of the employee
        """
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        """ Display details of the employee """
        super().display_details()
        print(f"Salary : {self.salary}\n")

