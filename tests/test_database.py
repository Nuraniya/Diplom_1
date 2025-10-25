import pytest
from database import Database


class TestDatabase:

    def test_database_initialization(self):
        db = Database()
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6