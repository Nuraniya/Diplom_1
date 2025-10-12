import pytest
from ingredient import Ingredient

class TestIngredient:

    def test_ingredient_initialization(self):
        ingredient = Ingredient("SAUCE", "кетчуп", 50)
        assert ingredient.type == "SAUCE"
        assert ingredient.name == "кетчуп"
        assert ingredient.price == 50

    def test_get_price(self):
        ingredient = Ingredient("FILLING", "котлета", 200)
        assert ingredient.get_price() == 200

    def test_get_name(self):
        ingredient = Ingredient("SAUCE", "майонез", 30)
        assert ingredient.get_name() == "майонез"

    def test_get_type(self):
        ingredient = Ingredient("FILLING", "сыр", 80)
        assert ingredient.get_type() == "FILLING"