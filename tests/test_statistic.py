# pylint: disable=line-too-long, missing-docstring
"""
Tests for the CalculationStatistic class.
"""

from decimal import Decimal
# import pytest
from calculator.statistic import CalculationStatistic


def dummy_operation(numbers: list[Decimal]) -> Decimal:
    """A dummy operation that returns the sum of the given numbers."""
    return sum(numbers)


def test_init_calculation_statistic():
    """Test initializing a CalculationStatistic instance directly."""
    a_list = [Decimal("1"), Decimal("2"), Decimal("3")]
    calc_stat = CalculationStatistic(a_list, dummy_operation)
    assert calc_stat.a == a_list
    assert calc_stat.b == 0
    assert calc_stat.operation is dummy_operation


def test_create_method():
    """Test that the static create method returns a proper CalculationStatistic instance."""
    a_list = [Decimal("4"), Decimal("5")]
    calc_stat = CalculationStatistic.create(a_list, dummy_operation)
    assert isinstance(calc_stat, CalculationStatistic)
    assert calc_stat.a == a_list
    assert calc_stat.b == 0
    assert calc_stat.operation is dummy_operation


def test_perform():
    """Test that perform() returns the correct result using the dummy operation."""
    a_list = [Decimal("1"), Decimal("2"), Decimal("3")]
    calc_stat = CalculationStatistic(a_list, dummy_operation)
    result = calc_stat.perform()
    # The dummy_operation sums the list: 1+2+3 = 6
    assert result == Decimal("6")


def test_repr():
    """Test that __repr__ returns the expected string representation."""
    a_list = [Decimal("10"), Decimal("20")]
    calc_stat = CalculationStatistic(a_list, dummy_operation)
    expected = f"CalculationStatistic({a_list}, 0, {dummy_operation.__name__})"
    assert repr(calc_stat) == expected
