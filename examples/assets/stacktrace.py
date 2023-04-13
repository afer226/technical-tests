from typing import Any, List


class ErrorTracing:
    """Contains exceptions for stack tracing"""

    def __init__(self):
        self._data: List[int] = [x for x in range(10) if x % 2 == 1]

    def add(self, value_to_add: Any):
        """
        Handles adding values to data.

        Args:
            value_to_add (int): The integer value to add.

        Raises:
            ValueError: If the value being added does not pass validations
        """
        self._validated_add(value_to_add)

        self._data.append(value_to_add)
        print(f"Added {value_to_add} successfully")
        print()

    def _validated_add(self, value_to_validate: Any):
        result = self._check_type(value_to_validate)
        self._check_even(result)
        self._check_is_not_33(result)

    def _check_type(self, value_to_validate: Any) -> int:
        if not isinstance(value_to_validate, int):
            raise ValueError("The value to add is an invalid type")

        return value_to_validate

    def _check_even(self, value_to_validated: int) -> int:
        if value_to_validated % 2 == 0:
            raise ValueError("The value to add is uneven")

    def _check_is_not_33(self, value_to_validated: int):
        if value_to_validated == 33:
            bad_error_message = "The letter being validated is invalid."
            raise (ValueError(bad_error_message))
