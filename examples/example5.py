import decimal

from examples.assets import abstract


def scenario1() -> None:
    """Example Usage"""
    myClass = abstract.Computer()
    myClass.display_message("Hello World", "Sam Powell")


def run():
    """
    Run the example below.

    In this example, the purpose of the code has purposefully be written to be difficult
    to understand.

    Try to determine what abstract.A() is meant to do.

    Rewrite A() so it is readable.
    Include documentation where possible

    Try to determine what real use this method could be used for.
    """
    print("EXAMPLE 5".center(80))

    scenario1()
