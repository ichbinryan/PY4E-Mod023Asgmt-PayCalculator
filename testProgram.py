import io
from random import randint
import random
from unittest.mock import Mock
import payCalculator

def test_payCalculator_prints_correct_result(capfd, monkeypatch):
    rate = float(randint(1, 100))
    hours = randint(1, 100)
    inp = [rate, hours]
    monkeypatch.setattr('builtins.input', lambda _:inp.pop())
    payCalculator.calculatePay()

    out, err = capfd.readouterr()
    expected = 'calculating pay\n{}\n'.format(rate * hours)
    assert out == expected
