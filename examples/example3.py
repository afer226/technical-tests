import decimal
import traceback

from examples.assets import inheritance


def assert_results(
    actual_salary: decimal,
    expected_salary: decimal,
    actual_post_tax: decimal,
    expected_post_tax: decimal,
    actual_weekly: decimal,
    expected_weekly: decimal,
    test_name: str,
) -> None:
    """
    Checks results

    Args:
        actual_salary (decimal): The salary amount we are testing against
        expected_salary (decimal): The expected value of the salary
        actual_post_tax (decimal): The post tax salary amount an employee earns
        expected_post_tax (decimal): The expected post tax amount
        actual_weekly (decimal): The weekly salary amount an employee earns
        expected_weekly (decimal): The expected weekly salary amount
        test_name (str): The name of the scenario
    """
    has_issue = False
    try:
        assert actual_salary == expected_salary, "Salary tested was incorrect."
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    try:
        assert actual_post_tax == expected_post_tax, "The post tax salary was incorrect"
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    try:
        assert actual_weekly == expected_weekly, "The weekly salary was incorrect"
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    if not has_issue:
        print(f"Passed {test_name}")
    else:
        print(f"Failed {test_name}")
    print()


def scenario1() -> None:
    """Implement the missing methods and inheritance structure"""
    name = "YOUR NAME HERE"
    age = 25
    salary: decimal = 50000
    employee = inheritance.Employee(name, age, salary)

    base_salary: decimal = employee.salary if hasattr(employee, "salary") else 0
    taxed_income: decimal = employee.salary_post_tax()
    weekly_taxed_income: decimal = employee.salary_post_tax()

    # Expected Values:
    expected_salary: decimal = 50000
    expected_taxed_income: decimal = 41980
    expected_weekly_taxed_income = 807.31

    assert_results(
        base_salary,
        expected_salary,
        taxed_income,
        expected_taxed_income,
        weekly_taxed_income,
        expected_weekly_taxed_income,
        "Scenario 1",
    )


def run():
    """Run the examples.

    In this example we ask you to implement the inheritance class.

    Please describe the improvements you made and why.
    """
    print("EXAMPLE 3".center(80))

    scenario1()

    import decimal
import traceback

from examples.assets import inheritance


def assert_results(
    actual_salary: decimal,
    expected_salary: decimal,
    actual_post_tax: float,
    expected_post_tax: float,
    actual_weekly: float,
    expected_weekly: float,
    test_name: str,
) -> None:
    """
    Checks results

    Args:
        actual_salary (decimal): The salary amount we are testing against
        expected_salary (decimal): The expected value of the salary
        actual_post_tax (decimal): The post tax salary amount an employee earns
        expected_post_tax (decimal): The expected post tax amount
        actual_weekly (decimal): The weekly salary amount an employee earns
        expected_weekly (decimal): The expected weekly salary amount
        test_name (str): The name of the scenario
    """
    has_issue = False
    
    try:
        assert actual_salary == expected_salary, "Salary tested was incorrect."
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    try:
        assert actual_post_tax == expected_post_tax, "The post tax salary was incorrect"
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    try:
        assert actual_weekly == expected_weekly, "The weekly salary was incorrect"
    except AssertionError as error:
        print(error)
        print(traceback.print_exc())
        print()
        has_issue = True

    if not has_issue:
        print(f"Passed {test_name}")
    else:
        print(f"Failed {test_name}")
    print()


def scenario1() -> None:
    """Implement the missing methods and inheritance structure"""
    name = "YOUR NAME HERE"
    age = 25
    salary: decimal = 50000
    employee = inheritance.Employee(name, age, salary)

    base_salary: decimal = employee.salary if hasattr(employee, "salary") else 0
    taxed_income: decimal = employee.salary_post_tax()
    weekly_taxed_income: float = employee.calculate_post_tax_weekly()

    # Expected Values:
    expected_salary: decimal = 50000
    expected_taxed_income: decimal = 41980.00
    expected_weekly_taxed_income = 807.31

    assert_results(
        base_salary,
        expected_salary,
        taxed_income,
        expected_taxed_income,
        weekly_taxed_income,
        expected_weekly_taxed_income,
        "Scenario 1",
    )


def run():
    """Run the examples.

    In this example we ask you to implement the inheritance class.

    Please describe the improvements you made and why.
    """
    print("EXAMPLE 3".center(80))

    scenario1()

    print()