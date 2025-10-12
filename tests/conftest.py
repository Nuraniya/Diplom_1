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