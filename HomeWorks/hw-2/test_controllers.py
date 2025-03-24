import pytest
from controllers import sum_operation
from pytest import approx


@pytest.mark.parametrize('a, b, expected', [
    (5, 6, 11),  # два положительных целых
    (-4, -9, -13),  # два отрицательных целых
    (7, -8, -1)  # положительное целое + отрицательное целое
])
def test_int_calculation_checker(a, b, expected):
    received = sum_operation(a, b)
    assert received == expected


@pytest.mark.parametrize('a, b, expected', [
    (5.3, 6.3, 11.6),  # два положительных с плавающей точкой
    (-4.4, -9.3, -13.7),  # два отрицательных с плавающей точкой
    (7.3, -8.9, -1.6)  # положительное с плавающей точкой + отрицательное с плавающей точкой
])
def test_float_calculation_checker(a, b, expected):
    received = sum_operation(a, b)
    assert received == approx(expected)


@pytest.mark.parametrize('a, b, expected', [
    (5, 6.3, 11.3),  # целое и положительное с плавающей точкой
    (-4, -9.3, -13.3),  # целое и отрицательное с плавающей точкой
    (7.0, -8, -1.0),  # положительное с плавающей точкой и отрицательное
    (0, -0.5, -0.5),  # целое  и отрицательное число с плавающей точкой
])
def test_mixed_calculation_checker(a, b, expected):
    received = sum_operation(a, b)
    assert received == approx(expected)


@pytest.mark.parametrize('a, b, expected', [
    (None, 5, None),  # первое значение None
    (5, None, None),  # второе значение None
    (None, None, None),  # оба значения None
])
def test_none_calculation_checker(a, b, expected):
    received = sum_operation(a, b)
    assert received == expected
