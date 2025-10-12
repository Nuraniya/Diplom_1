import pytest
from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_new_burger_bun_is_none(self, burger):
        assert burger.bun is None

    def test_new_burger_ingredients_empty(self, burger):
        assert burger.ingredients == []

    def test_set_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_increases_count(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_stores_correct_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_decreases_count(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_keeps_correct_ingredient(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert burger.ingredients[0] == ingredient2

    def test_cannot_remove_from_empty_burger(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_changes_order(self, burger):
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)
        assert burger.ingredients[0] == ingredient2

    def test_calculate_price_with_bun_and_ingredients(self, burger, mock_bun):
        mock_bun.get_price.return_value = 50
        ingredient = Mock()
        ingredient.get_price.return_value = 30
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 130

    def test_calculate_price_with_only_bun(self, burger, mock_bun):
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200

    def test_cannot_calculate_price_without_bun(self, burger):
        ingredient = Mock()
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_receipt_contains_bun_name(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert "красная булочка" in receipt

    def test_receipt_contains_sauce_ingredient(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        mock_bun.get_price.return_value = 100
        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "острый соус"
        sauce.get_price.return_value = 50
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert "острый соус" in receipt

    def test_receipt_contains_filling_ingredient(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        mock_bun.get_price.return_value = 100
        cutlet = Mock()
        cutlet.get_type.return_value = "FILLING"
        cutlet.get_name.return_value = "котлета"
        cutlet.get_price.return_value = 150
        burger.set_buns(mock_bun)
        burger.add_ingredient(cutlet)
        receipt = burger.get_receipt()
        assert "котлета" in receipt

    def test_receipt_contains_correct_price(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        mock_bun.get_price.return_value = 100
        sauce = Mock()
        sauce.get_price.return_value = 50
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert "Price: 250" in receipt

    def test_cannot_get_receipt_without_bun(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()

    @pytest.mark.parametrize("bun_price,ingredients_count,ingredient_price,expected", [
        (100, 0, 0, 200),
        (50, 1, 30, 130),
        (80, 2, 20, 200),
    ])
    def test_price_calculation(self, burger, mock_bun, bun_price, ingredients_count, ingredient_price, expected):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)
        for _ in range(ingredients_count):
            ingredient = Mock()
            ingredient.get_price.return_value = ingredient_price
            burger.add_ingredient(ingredient)
        assert burger.get_price() == expected