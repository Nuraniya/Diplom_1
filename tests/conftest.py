import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from unittest.mock import Mock


@pytest.fixture
def burger():
    from burger import Burger
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "обычная булочка"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def burger_with_ingredients(burger):
    ingredient1 = Mock()
    ingredient2 = Mock()
    ingredient1.get_price.return_value = 50
    ingredient2.get_price.return_value = 50
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    return burger


@pytest.fixture
def burger_with_three_ingredients(burger):
    ingredient1 = Mock()
    ingredient2 = Mock()
    ingredient3 = Mock()
    ingredient1.get_price.return_value = 50
    ingredient2.get_price.return_value = 50
    ingredient3.get_price.return_value = 50
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    burger.add_ingredient(ingredient3)
    return burger