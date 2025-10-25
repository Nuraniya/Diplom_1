import pytest
import sys
from unittest.mock import patch, Mock


class TestPraktikum:

    def test_main_calls_print_with_receipt(self):
        with patch('database.Database') as mock_db:
            with patch('burger.Burger') as mock_burger_class:
                with patch('builtins.print') as mock_print:
                    mock_db_instance = mock_db.return_value
                    mock_burger_instance = mock_burger_class.return_value

                    mock_bun = Mock()
                    mock_ingredients = [Mock() for _ in range(6)]

                    mock_db_instance.available_buns.return_value = [mock_bun]
                    mock_db_instance.available_ingredients.return_value = mock_ingredients
                    mock_burger_instance.get_receipt.return_value = "Test receipt"

                    import praktikum
                    praktikum.main()

                    mock_print.assert_called_once_with("Test receipt")

    def test_praktikum_main_execution(self):
        original_argv = sys.argv
        sys.argv = ['praktikum.py']

        with patch('database.Database') as mock_db, \
                patch('burger.Burger') as mock_burger, \
                patch('builtins.print'):
            mock_db_instance = mock_db.return_value
            mock_db_instance.available_buns.return_value = [Mock()]
            mock_db_instance.available_ingredients.return_value = [Mock() for _ in range(6)]

            import praktikum
            praktikum.main()

        sys.argv = original_argv

        assert True