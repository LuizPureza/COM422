import pytest
from Person import Person

def test_create_person():
    p1 = Person("abc", 150, 50, 40)
    assert p1.name == "abc"
    assert p1.weight == 150

def test_run_energy_changes():
    p1 = Person("abc", 150, 50, 40)
    p1.run(5)
    assert p1.energy == 30

def test_run_hunger_changes():
    p1 = Person("abc", 150, 50, 40)
    p1.run(5)
    assert p1.hunger == 60

def test_run_returns_true():
    p1 = Person("abc", 150, 50, 40)
    assert p1.run(5) == True
    assert p1.energy == 30

