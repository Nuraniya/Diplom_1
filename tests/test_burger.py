import pytest
from unittest.mock import Mock
from burger import Burger


class TestBurger:

    def test_bun_is_none_when_burger_created(self, burger):
        assert burger.bun is None

    def test_ingredients_list_is_empty_when_burger_created(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_bun_correctly(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_increases_ingredients_count(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1

    def test_add_ingredient_stores_ingredient_correctly(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient_decreases_ingredients_count(self, burger_with_ingredients):
        initial_count = len(burger_with_ingredients.ingredients)
        burger_with_ingredients.remove_ingredient(0)
        assert len(burger_with_ingredients.ingredients) == initial_count - 1

    def test_remove_ingredient_removes_correct_ingredient(self, burger_with_ingredients):
        initial_second_ingredient = burger_with_ingredients.ingredients[1]
        burger_with_ingredients.remove_ingredient(0)
        assert burger_with_ingredients.ingredients[0] == initial_second_ingredient

    def test_remove_ingredient_raises_error_when_index_out_of_range(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(0)

    def test_move_ingredient_changes_ingredients_order(self, burger_with_three_ingredients):
        initial_first_ingredient = burger_with_three_ingredients.ingredients[0]
        burger_with_three_ingredients.move_ingredient(0, 2)
        assert burger_with_three_ingredients.ingredients[0] != initial_first_ingredient

    def test_get_price_returns_correct_price_with_bun_and_ingredients(self, burger, mock_bun):
        mock_bun.get_price.return_value = 50
        ingredient = Mock()
        ingredient.get_price.return_value = 30
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient)
        assert burger.get_price() == 130

    def test_get_price_returns_correct_price_with_only_bun(self, burger, mock_bun):
        mock_bun.get_price.return_value = 100
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200

    def test_get_price_raises_error_when_bun_not_set(self, burger):
        ingredient = Mock()
        ingredient.get_price.return_value = 50
        burger.add_ingredient(ingredient)
        with pytest.raises(AttributeError):
            burger.get_price()

    def test_receipt_starts_with_bun_name(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert receipt.startswith("(==== красная булочка ====)")

    def test_receipt_contains_ingredient_lines(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        mock_bun.get_price.return_value = 100

        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "острый соус"
        sauce.get_price.return_value = 50

        cutlet = Mock()
        cutlet.get_type.return_value = "FILLING"
        cutlet.get_name.return_value = "котлета"
        cutlet.get_price.return_value = 50

        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        burger.add_ingredient(cutlet)

        receipt = burger.get_receipt()

        expected_receipt = (
            "(==== красная булочка ====)\n"
            "= sauce острый соус =\n"
            "= filling котлета =\n"
            "(==== красная булочка ====)\n\n"
            "Price: 300"
        )
        assert receipt == expected_receipt

    def test_receipt_ends_with_correct_price(self, burger, mock_bun):
        mock_bun.get_name.return_value = "красная булочка"
        mock_bun.get_price.return_value = 100
        sauce = Mock()
        sauce.get_type.return_value = "SAUCE"
        sauce.get_name.return_value = "острый соус"
        sauce.get_price.return_value = 50
        burger.set_buns(mock_bun)
        burger.add_ingredient(sauce)
        receipt = burger.get_receipt()
        assert receipt.endswith("Price: 250")

    def test_get_receipt_raises_error_when_bun_not_set(self, burger):
        with pytest.raises(AttributeError):
            burger.get_receipt()