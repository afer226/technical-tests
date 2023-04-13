# n3 Hub Technical Test

Answered by Ash Fernandes, 14/04/23

## Example 1 - Stack Tree

### Scenario 1

* Valid as it passes all checks:  ``_check_type``, ``_check_even``, and ``_check_is_not_33``.

### Scenario 2

* Invalid as it is of type ``string``, hence failing the check: ``_check_type()``.

### Scenario 3

* Invalid as it fails the check: ``_check_even``.

### Scenario 4

* Invalid as it fails the check: ``_check_is_not_33``.

## Example 2 - Performance

    def add2(self, value_to_add: int):
        """
        Write your own method for adding a value as efficiently as possible.

        Args:
            value_to_add (int): The value to add
        """
        start = time.time()

        if value_to_add not in self._data:
            self._data.append(value_to_add)
            print(f"Added {value_to_add}")

        end = time.time()

        return end - start, self._data

The ``add2()`` function skips checking whether an item (``value``) in ``self._data`` is equivalent to ``value_to_add``, and if not a duplicate, appends ``value_to_add`` to ``self._data``. This greatly increases the efficiency of the function.

## Example 3 - Inheritance

``NOTE:`` Unfortunately was unable to complete this question due to time constraints. Here is my ``Employee`` class however, producing errors.

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

## Example 4 - Validation

    def _withdraw_validations(self, amount_to_withdraw: decimal) -> bool:
        """
        Validates the withdrawal against this persons bank account.

        Args:
            amount_to_withdraw (decimal): The amount being requested
        """

        if amount_to_withdraw <= 0:
            error_message = "You may not withdraw an amount less than or equal to 0."
            raise ValidationException(error_message)
        
        limit = self.amount + self.overdraft

        if amount_to_withdraw > limit:
            error_message = "You may not withdraw more than {} dollars.".format(limit)
            raise ValidationException(error_message)
        
        pass

``Extra:`` Modified first ``if`` statement to prevent withdrawing zero dollars as this is unfeasable.

## Example 5 - Abstract

I have renamed this class to ``Computer`` since it features sign-in/out and messaging capabilities.

Two exceptions exist: 

1. ``SignInException`` gets raised when a different user is using this system and someone else wants to sign in.

2. ``MessageException`` gets raised when a message is not displayed properly (e.g. has no content).