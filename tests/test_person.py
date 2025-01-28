import pytest
from Person import Person

def test_create_person():
    p1 = Person("abc", 150, 50, 40)
    assert p1.name == "abc"

def test_sad():
    p1 = Person("abc", 150, 50, 40)
    assert p1.hunger == 50

def test_run_return_false_energy():
    p1 = Person("abc", 150, 50, 40)
    assert p1.run(20) == False