def test_subtract_operation():
    op = SubtractOperation(10, 1, 3, 2, 1)
    assert op.operate() == 3
