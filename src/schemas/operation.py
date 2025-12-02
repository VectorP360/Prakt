class OperationOut:
    def __init__(self, operation_id: int, name: str):
        self.operation_id = operation_id
        self.name = name

class OperationIn:
    def __init__(self, name: str):
        self.name = name
