from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_database_initialization(self):
        """Тест инициализации объекта Database"""
        database = Database()

        # Проверка наличия булочек
        assert len(database.buns) == 3
        assert isinstance(database.buns[0], Bun)
        assert database.buns[0].get_name() == "black bun"
        assert database.buns[1].get_name() == "white bun"
        assert database.buns[2].get_name() == "red bun"

        # Проверка наличия ингредиентов
        assert len(database.ingredients) == 6
        assert isinstance(database.ingredients[0], Ingredient)

        # Проверка соусов
        sauce_count = sum(1 for ingredient in database.ingredients
                          if ingredient.get_type() == INGREDIENT_TYPE_SAUCE)
        assert sauce_count == 3

        # Проверка начинок
        filling_count = sum(1 for ingredient in database.ingredients
                            if ingredient.get_type() == INGREDIENT_TYPE_FILLING)
        assert filling_count == 3

    def test_available_buns(self):
        """Тест метода available_buns"""
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns == database.buns

    def test_available_ingredients(self):
        """Тест метода available_ingredients"""
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        assert ingredients == database.ingredients