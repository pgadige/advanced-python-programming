def test_calculator_with_multiple_operations():
    calc = Calculator(
        operations={
            'add': AddOperation,
            'subtract': SubtractOperation
        }
    )
    assert calc.calculate(1, 5, 13, 2, 'add') == 21
    assert calc.calculate(13, 3, 7, 'subtract') == 3
