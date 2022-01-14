from unittest.mock import Mock, patch
import payCalculator


def test_payCalculator_prints_correct_result(capfd):
    payCalculator.input = lambda: '123'
    payCalculator.calculatePay()

    # //out, err = capfd.readouterr()
    # //print(out)
    # assert out == '15129'
