# pylint: disable=invalid-name, line-too-long
"""
Testing the operations module.
"""

from decimal import Decimal

import pytest

from calculator.operations import (
    add, subtract, multiply, divide, mean, median, mode
)
from calculator.calculation import Calculation


# --- Binary Arithmetic Operations ---


def test_add_operation(faker):
    """Test the addition operation."""
    a = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    b = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    expected = a + b
    calculation = Calculation.create(a, b, add)
    assert calculation.perform() == expected, (
        f"add operation failed for {a} and {b}"
    )


def test_subtract_operation(faker):
    """Test the subtraction operation."""
    a = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    b = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    expected = a - b
    calculation = Calculation.create(a, b, subtract)
    assert calculation.perform() == expected, (
        f"subtract operation failed for {a} and {b}"
    )


def test_multiply_operation(faker):
    """Test the multiplication operation."""
    a = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    b = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    expected = a * b
    calculation = Calculation.create(a, b, multiply)
    assert calculation.perform() == expected, (
        f"multiply operation failed for {a} and {b}"
    )


def test_divide_operation(faker):
    """Test the division operation."""
    a = Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
    b = Decimal(
        str(
            faker.pydecimal(
                min_value=Decimal("0.1"), left_digits=2, right_digits=2, positive=True
            )
        )
    )
    expected = a / b
    calculation = Calculation.create(a, b, divide)
    assert calculation.perform() == expected, (
        f"divide operation failed for {a} and {b}"
    )


def test_divide_by_zero():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation.create(Decimal("10"), Decimal("0"), divide)
        calculation.perform()


# --- Statistic Operations ---


def test_mean_operation(faker):
    """Test the mean operation with a non-empty list."""
    values = [
        Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
        for _ in range(5)
    ]
    expected = sum(values) / Decimal(len(values))
    result = mean(values)
    assert result == expected, f"mean operation failed for list {values}"


def test_mean_empty_list():
    """Test that computing the mean of an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate the mean of an empty list"):
        mean([])


def test_median_operation_odd(faker):
    """Test the median operation for an odd-length list."""
    values = sorted(
        [
            Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
            for _ in range(5)
        ]
    )
    expected = values[len(values) // 2]
    result = median(values)
    assert result == expected, f"median operation failed for odd list {values}"


def test_median_operation_even(faker):
    """Test the median operation for an even-length list."""
    values = sorted(
        [
            Decimal(str(faker.pydecimal(left_digits=2, right_digits=2, positive=True)))
            for _ in range(4)
        ]
    )
    expected = (values[1] + values[2]) / 2
    result = median(values)
    assert result == expected, f"median operation failed for even list {values}"


def test_median_empty_list():
    """Test that computing the median of an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate the median of an empty list"):
        median([])


def test_mode_operation_single_mode():
    """Test the mode operation for a list with a single mode."""
    values = [Decimal("5"), Decimal("5"), Decimal("3"), Decimal("7")]
    result = mode(values)
    assert result == Decimal("5"), f"mode operation failed for single mode in list {values}"


def test_mode_operation_multiple_modes():
    """Test the mode operation for a list with multiple modes."""
    values = [Decimal("1"), Decimal("2"), Decimal("1"), Decimal("2")]
    result = mode(values)
    assert isinstance(result, list), "mode should return a list when there are multiple modes"
    assert Decimal("1") in result and Decimal("2") in result, (
        f"mode operation failed for multiple modes in list {values}"
    )


def test_mode_empty_list():
    """Test that computing the mode of an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate the mode of an empty list"):
        mode([])
