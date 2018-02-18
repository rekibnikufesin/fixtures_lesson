"""
Tests for Car class
"""

import pytest
from car import Car

class TestCar(object):

    @pytest.fixture(scope="module")
    def my_car(self):
        return Car(0, "off")

    def test_start(self, my_car):
        my_car.start()
        assert my_car.state == "running"

    def test_turn_off(self, my_car):
        my_car.turn_off()
        assert my_car.state == "off"

    def test_accelerate(self, my_car):
        my_car.accelerate()
        assert my_car.speed == 10

    def test_accelerate1(self, my_car):
        my_car.accelerate()
        assert my_car.speed == 10

    def test_stop(self, my_car):
        my_car.stop()
        assert my_car.speed == 0
