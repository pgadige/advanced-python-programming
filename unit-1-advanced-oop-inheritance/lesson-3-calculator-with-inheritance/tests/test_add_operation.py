def test_add_operation():
    op = AddOperation(5, 1, 8, 3, 2)
    assert op.operate() == 19
