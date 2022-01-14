import io
from random import randint
from unittest.mock import Mock
import payCalculator

input_1 = Mock()
input_1.return_value = '15'
input_2 = Mock()
input_2.return_value = '27'

input_mock = Mock()
input_mock.side_effect = [input_1, input_2]


def test_payCalculator_prints_correct_result(capfd, monkeypatch):
    inp = randint(1, 100)
    monkeypatch.setattr('builtins.input', lambda _:inp)
    payCalculator.calculatePay()

    out, err = capfd.readouterr()
    print(out)
    assert out == 'calculating pay\n{}\n'.format(inp**2)
