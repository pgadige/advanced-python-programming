class OperationInvalidException(Exception):
    pass


class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):

    def operate(self):
        return sum(self.args)


class SubtractOperation(Operation):

    def operate(self):
        if not self.args:
            return 0
        return self.args[0] - sum(self.args[1:])


class Calculator(object):

    def __init__(self, operations):
        self.operations = operations

    def calculate(self, *args):
        numbers, operation = args[:-1], args[-1]
        if operation not in self.operations:
            raise OperationInvalidException
        operation = self.operations[operation](*numbers)
        return operation.operate()
