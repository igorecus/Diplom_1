import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    """Тесты для класса Ingredient"""

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)])

    def test_ingredient_initialization(self, ingredient_type, name, price):
        """Тест инициализации объекта Ingredient"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self):
        """Тест метода get_price"""
        amount = 300.0
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", amount)
        assert ingredient.get_price() == amount

    def test_get_name(self):
        """Тест метода get_name"""
        sauce_name = "hot sauce"
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, sauce_name, 100.0)
        assert ingredient.get_name() == sauce_name

    def test_get_type(self):
        """Тест метода get_type"""
        filling = INGREDIENT_TYPE_FILLING
        ingredient = Ingredient(filling, "sausage", 300.0)
        assert ingredient.get_type() == filling
