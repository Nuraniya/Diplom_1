import pytest
import subprocess
import sys
import os
from unittest.mock import patch, Mock


def test_main_execution_as_script():
    with patch('database.Database') as mock_db:
        with patch('burger.Burger') as mock_burger_class:
            with patch('builtins.print') as mock_print:
                mock_db_instance = mock_db.return_value
                mock_burger_instance = mock_burger_class.return_value

                mock_bun = Mock()
                mock_bun.get_name.return_value = "black bun"
                mock_bun.get_price.return_value = 100

                mock_ingredients = [Mock() for _ in range(6)]
                for i, ingredient in enumerate(mock_ingredients):
                    ingredient.get_name.return_value = f"ingredient_{i}"
                    ingredient.get_price.return_value = 50
                    ingredient.get_type.return_value = "SAUCE" if i % 2 == 0 else "FILLING"

                mock_db_instance.available_buns.return_value = [mock_bun]
                mock_db_instance.available_ingredients.return_value = mock_ingredients
                mock_burger_instance.get_receipt.return_value = "Test receipt"

                import praktikum
                praktikum.main()

                mock_print.assert_called_once_with("Test receipt")


def test_direct_main_execution():
    original_argv = sys.argv

    try:
        sys.argv = ['praktikum.py']

        with patch('database.Database') as mock_db:
            mock_db_instance = mock_db.return_value
            mock_db_instance.available_buns.return_value = [Mock()]
            mock_db_instance.available_ingredients.return_value = [Mock() for _ in range(6)]

            with patch('burger.Burger'):
                with patch('builtins.print') as mock_print:
                    import importlib.util

                    spec = importlib.util.spec_from_file_location(
                        "__main__",
                        os.path.join(os.path.dirname(__file__), '..', 'praktikum.py')
                    )
                    module = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(module)

                    assert mock_print.called, "Print was not called during main execution"

    finally:
        sys.argv = original_argv