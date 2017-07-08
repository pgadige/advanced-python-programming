import pytest

def test_calculator_invoked_with_an_invalid_operation():
    calc = Calculator(
        operations={
            'add': AddOperation
        }
    )
    with pytest.raises(OperationInvalidException, message='Expecting OperationInvalidException'):
        res = calc.calculate(1, 5, 13, 2, 'INVALID')
