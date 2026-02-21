import pytest
from my_project.src.app import add, sub, multipuly, division
from my_project.src.app import calccc

# def test_add():
#     result = add(2,3)
#     assert result == 6

# def test_sub():
#     result = sub(2,3)
#     assert result == -1

# def test_mul():
#     result = multipuly(2,3)
#     assert result == 6

# def test_dev():
#     result = division(10,5)
#     assert result == 2
'''
def test_calc():
    assert add(1,2)==3
    assert sub(9,1)==8
    assert multipuly(3,4)==12

def test_calc_add():
    assert add(1,2)==3
    assert add(9,1)==10
    assert add(3,4)==7'''

# pytest fixture
# @pytest.fixture
# def calc():
#     return calccc()

# def test_calc_add(calc):
#     assert calc.add(1,2)==3

# parametrized test
# @pytest.mark.parametrize("a,b,expected", [
#     (1,2,3),
#     (9,1,10),
#     (3,4,7)
# ])
# def test_calc_add_param(calc,a,b,expected):
#     assert calc.add(a,b)==expected

# testing exceptions
def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(10,0)
    




