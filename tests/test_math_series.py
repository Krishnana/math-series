from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.mark.parametrize("test_input,expected",[(1,1),(2,1),(3,2),(4,3),(5,5),(6,8)])
def test_fibonnaci(test_input,expected):
    assert fibonacci(test_input) == expected

@pytest.mark.parametrize("test_input,expected",[(0,2),(1,1),(2,3),(3,4),(4,7),(5,11)])
def test_lucas(test_input,expected):
    assert lucas(test_input) == expected

@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected",[(1,0,1,1),(2,0,1,1),(3,0,1,2),(4,0,1,3),(5,0,1,5),(6,0,1,8)])
def test_fibonnaci_using_sum(test_input1,test_input2,test_input3,expected):
    assert sum_series(test_input1,test_input2,test_input3) == expected

@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected",[(0,2,1,2),(1,2,1,1),(2,2,1,3),(3,2,1,4),(4,2,1,7),(5,2,1,11)])
def test_lucas_using_sum(test_input1,test_input2,test_input3,expected):
    assert sum_series(test_input1,test_input2,test_input3) == expected