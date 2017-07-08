def test_calculator_with_one_operation():
    calc = Calculator(
        operations={
            'add': AddOperation
        }
    )

    assert calc.calculate(1, 5, 13, 2, 'add') == 21
