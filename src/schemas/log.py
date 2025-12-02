from .user import UserOut
from .operation import OperationOut

class LogOut:
    def __init__(
        self,
        log_id: int,
        operation_date: str,
        user: UserOut,
        operation: OperationOut
    ):
        self.log_id = log_id
        self.operation_date = operation_date
        self.user = user
        self.operation = operation


class LogIn:
    def __init__(
        self,
        operation_date: str,
        user: UserOut,
        operation: OperationOut
    ):
        self.operation_date = operation_date
        self.user = user
        self.operation = operation
