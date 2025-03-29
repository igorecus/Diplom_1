import pytest
from unittest.mock import Mock
from burger import Burger
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    """Тесты для класса Burger"""

    def test_burger_initialization(self):
        """Тест инициализации объекта Burger"""
        burger = Burger()
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        """Тест установки булочек"""
        burger = Burger()
        bun = Mock()
        bun.get_name.return_value = "black bun"
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        """Тест добавления ингредиента"""
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        """Тест удаления ингредиента"""
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient2

    def test_move_ingredient(self):
        """Тест перемещения ингредиента"""
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        burger.move_ingredient(0, 2)

        assert burger.ingredients[0] == ingredient2
        assert burger.ingredients[1] == ingredient3
        assert burger.ingredients[2] == ingredient1

    def test_get_price(self):
        """Тест получения цены бургера"""
        burger = Burger()

        bun = Mock()
        bun.get_price.return_value = 43.0

        ingredient1 = Mock()
        ingredient1.get_price.return_value = 17.0

        ingredient2 = Mock()
        ingredient2.get_price.return_value = 25.3

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_price = 43.0 * 2 + 17 + 25.3
        assert burger.get_price() == expected_price

    def test_get_receipt(self):
        """Тест получения чека"""
        burger = Burger()

        bun = Mock()
        bun.get_name.return_value = "white bun"
        bun.get_price.return_value = 200

        ingredient1 = Mock()
        ingredient1.get_name.return_value = "Cutlet"
        ingredient1.get_price.return_value = 100
        ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING

        ingredient2 = Mock()
        ingredient2.get_name.return_value = "Hot Sauce"
        ingredient2.get_price.return_value = 100
        ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE

        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        receipt = burger.get_receipt()

        assert "(==== white bun ====)" in receipt
        assert "= filling Cutlet =" in receipt
        assert "= sauce Hot Sauce =" in receipt
        assert "Price: 600" in receipt