import pytest
from bun import Bun

class TestBun:

    def test_bun_initialization(self):
        bun = Bun("черная булочка", 100)
        assert bun.name == "черная булочка"
        assert bun.price == 100

    def test_get_name(self):
        bun = Bun("белая булочка", 200)
        assert bun.get_name() == "белая булочка"

    def test_get_price(self):
        bun = Bun("красная булочка", 150)
        assert bun.get_price() == 150