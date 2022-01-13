import payCalculator
import unittest

@unittest.mock.patch('payCalculator.input', create=True)
def test_payCalculator_prints_correct_result(capfd, mocked_input):
    ['15', '145.73']
    payCalculator.calculatePay()

    out, err = capfd.readouterr()
    print(out)
    assert out == '2185.95'
