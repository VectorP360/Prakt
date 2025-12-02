from logging import Handler, Formatter, getLogger, DEBUG
from datetime import datetime

from src.schemas.log import LogIn
from src.schemas.user import UserOut

from src.repositories.repository import RepositoryManager

formatter = Formatter('%(message)s')

class MEGA_LOGGER_40000():
    def __init__(self, manager: RepositoryManager):
        self.manager = manager
        self.operation_repository = manager.get_operation_repository()
        self.logger = getLogger(__name__)
        self.logger.setLevel(level=DEBUG)
        self.dbh = DBHandler(manager = self.manager)
        self.dbh.setFormatter
        self.dbh.setLevel(DEBUG)
        self.logger.addHandler(self.dbh)

    def log(self, user: UserOut, operation: str):
        operation_to_log = self.operation_repository.get_by_name(operation)
        self.logger.debug("%s %s", user.user_id, operation_to_log.operation_id)



class DBHandler(Handler):
    def __init__(self, manager: RepositoryManager):
        self.manager = manager
        self.log_repository = manager.get_log_repository()
        self.user_repository = manager.get_user_repository()
        self.operation_repository = manager.get_operation_repository()
        self.filters=[]
        self.lock = None
        self.formatter = formatter

    def emit(self, record):
        log_entry = self.format(record=record)
        log_entry = log_entry.split(sep=None)
        user = self.user_repository.get_by_ID(log_entry[0])
        operation = self.operation_repository.get_by_id(log_entry[1])
        self.log_repository.create(log_in=LogIn(operation_date=datetime.now(), user=user, operation=operation))
        
