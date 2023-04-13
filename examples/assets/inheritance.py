import decimal


class Person:
    name: str = ""
    age: int = int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Employee(Person):
    salary: int = int

    def __init__(self, name: str, age: int, salary: int) -> None:
        # TODO: Call base class and instantiate attributes.
        # TODO: Salary is the annual amount paid to an employee
        self.name = name
        self.age = age
        self.salary = salary
        self.salary_post_tax = None
        
    def calculate_weekly(self) -> decimal:
        """
        Calculate the weekly payment to a worker after taxes."""
        # TODO: Calculate weekly payment to a worker after taxes applied.
        # For simplicity, please use 52 weeks in a year.
        # Please round to the nearest cent.
        
        salary = self.calculate_post_tax()

        return round(salary / 52, 2) 

    def calculate_post_tax_weekly(self) -> decimal:
        """Calculate the tax obligation of an employee."""
        # Apply Tax rates (10.5, 17.5, 30, 33, 39)
        # https://tinyurl.com/y34xm2tv
        # TODO: Calculate the tax obligation of a worker from their salary
        # Use the tax brackets provided in the above link

        if self.salary <= 14000:
            calculate_post_tax = self.salary - (self.salary * .105)

        if self.salary >= 14001 and self.salary <= 48000:
            self.calculate_post_tax = self.salary - (1470 + (self.salary * .175))

        if self.salary >= 48001 and self.salary <= 70000:
            self.calculate_post_tax = self.salary - (7420 + (self.salary * .3))

        if self.salary >= 70001 and self.salary <= 180000:
            self.calculate_post_tax = self.salary - (14020 + (self.salary * .33))

        if self.salary >= 180000:
            self.calculate_post_tax = self.salary - (50320 + (self.salary * .105))

        return round(self.calculate_post_tax, 2)