# Hint: don't forget the custom exception


class Operation(object):
    def __init__(self, *args):
        # Do something here
        pass

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        pass


class SubtractOperation(Operation):
    def operate(self):
        pass


class Calculator(object):
    pass
