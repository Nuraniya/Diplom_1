import pytest
from bun import Bun
from data import TestData


class TestBun:

    def test_bun_name_after_initialization(self):
        bun = Bun(TestData.BUN_NAMES[0], TestData.BUN_PRICES[0])
        assert bun.name == TestData.BUN_NAMES[0]

    def test_bun_price_after_initialization(self):
        bun = Bun(TestData.BUN_NAMES[0], TestData.BUN_PRICES[0])
        assert bun.price == TestData.BUN_PRICES[0]

    def test_get_name_returns_correct_name(self):
        bun = Bun(TestData.BUN_NAMES[1], TestData.BUN_PRICES[1])
        assert bun.get_name() == TestData.BUN_NAMES[1]

    def test_get_price_returns_correct_price(self):
        bun = Bun(TestData.BUN_NAMES[2], TestData.BUN_PRICES[2])
        assert bun.get_price() == TestData.BUN_PRICES[2]