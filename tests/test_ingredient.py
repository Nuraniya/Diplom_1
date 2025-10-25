import pytest
from ingredient import Ingredient
from data import TestData


class TestIngredient:

    def test_ingredient_type_after_initialization(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPES[0], TestData.INGREDIENT_NAMES[0], TestData.INGREDIENT_PRICES[0])
        assert ingredient.type == TestData.INGREDIENT_TYPES[0]

    def test_ingredient_name_after_initialization(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPES[0], TestData.INGREDIENT_NAMES[0], TestData.INGREDIENT_PRICES[0])
        assert ingredient.name == TestData.INGREDIENT_NAMES[0]

    def test_ingredient_price_after_initialization(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPES[0], TestData.INGREDIENT_NAMES[0], TestData.INGREDIENT_PRICES[0])
        assert ingredient.price == TestData.INGREDIENT_PRICES[0]

    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPES[1], TestData.INGREDIENT_NAMES[3], TestData.INGREDIENT_PRICES[3])
        assert ingredient.get_price() == TestData.INGREDIENT_PRICES[3]

    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPES[0], TestData.INGREDIENT_NAMES[1], TestData.INGREDIENT_PRICES[1])
        assert ingredient.get_name() == TestData.INGREDIENT_NAMES[1]

    def test_get_type_returns_correct_type(self):
        ingredient = Ingredient(TestData.INGREDIENT_TYPES[1], TestData.INGREDIENT_NAMES[4], TestData.INGREDIENT_PRICES[4])
        assert ingredient.get_type() == TestData.INGREDIENT_TYPES[1]