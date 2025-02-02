import pytest
from Person import Person

class TestPerson:

    def test_rest_energy_changes(self):
        p1 = Person("abc", 150, 99, 1)
        p1.rest()
        assert p1.energy == 2

    def test_rest_hunger_changes2(self):
        p1 = Person("abc", 150, 99, 1)
        p1.rest()
        assert p1.hunger == 100

