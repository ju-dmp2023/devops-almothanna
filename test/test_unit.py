import pytest
from calculator_helper import CalculatorHelper

class BaseTest:
    def setup_method(self):
        self.calc = CalculatorHelper()

    def teardown_method(self):
        self.calc = None

class TestCalculator(BaseTest):
    
    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 6),
        (3, -3, 0)
    ])
    def test_add(self, a, b, expected):
        assert self.calc.add(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 5, 5),
        (0, 5, -5)
    ])
    def test_subtract(self, a, b, expected):
        assert self.calc.subtract(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (3, 3, 9),
        (3, -3, -9)
    ])
    def test_multiply(self, a, b, expected):
        assert self.calc.multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),
        (9, 3, 3)
    ])
    def test_divide(self, a, b, expected):
        assert self.calc.divide(a, b) == expected

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(10, 0)