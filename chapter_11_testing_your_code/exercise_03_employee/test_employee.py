import pytest
from employee import Employee


@pytest.fixture
def employee():
    return Employee("Andreas", "Landerer", 100_000)


def test_give_default_raise(employee):
    base_salary = employee.salary
    expected_salary = base_salary + 5_000
    employee.give_raise()
    assert expected_salary == employee.salary


def test_give_custom_raise(employee):
    base_salary = employee.salary
    custom_raise = 12_000
    expected_salary = base_salary + custom_raise
    employee.give_raise(custom_raise)
    assert expected_salary == employee.salary
