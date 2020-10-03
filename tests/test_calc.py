from Calc.calculator import Calculator
import pytest


def test_add():
    cal = Calculator()
    assert cal.add(25.16, 32.17) == 57.33


def test_add_with_char_exception():
    cal = Calculator()
    with pytest.raises(Exception):
        assert cal.add("twenty two", 32.17)


def test_substract():
    cal = Calculator()
    assert round(cal.substract(25.16, 32.17),2) == -7.01


def test_multiply():
    cal = Calculator()
    assert cal.multiply(12.17, 10) == 121.7


def test_divide():
    cal = Calculator()
    assert cal.divide(75.5, 5) == 15.1


def test_divide_by_zero():
    cal = Calculator()
    with pytest.raises(Exception):
        assert cal.divide(1, 0.0)


def test_power():
    cal = Calculator()
    assert cal.power(3, 4) == 81
