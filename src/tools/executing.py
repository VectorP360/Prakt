import logging

from src.repositories.repository import RepositoryManager

from src.clients.user_terminal_client import UserTerminalClient
from src.clients.leader_choice_client import LeaderClient
from src.clients.worker_client import WorkerClient
from src.enums.post import UserPost
from src.tools.sing_up import SingUp
from tools.db_logger import DBHandler


class Executer:
    def __init__(self, manager: RepositoryManager):
        self.manager = manager
        self.operation_repository = manager.get_operation_repository()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level=logging.DEBUG)
        self.dbh = DBHandler(manager = self.manager)
        self.dbh.setFormatter
        self.dbh.setLevel(logging.DEBUG)
        self.logger.addHandler(self.dbh)

    def execute(self):
        user = SingUp(self.manager).singing_up()

        if user:
            operation_to_log = self.operation_repository.get_by_name("LOGIN")
            self.logger.debug("%s %s", user.user_id, operation_to_log.operation_id)
            match user.post.name:
                case UserPost.FIRST_CATEGORY.value:
                    client = WorkerClient(manager=self.manager, user=user)
                    client.run()

                case UserPost.SENIOR.value:
                    client = UserTerminalClient(manager=self.manager, user=user)
                    client.run()

                case UserPost.MAIN_EXPERT.value:
                    client = LeaderClient(manager=self.manager, user=user).run()
                    if client:
                        client.run()

                case UserPost.DIRECTOR.value:
                    client = LeaderClient(manager=self.manager,user=user).run()
                    if client:
                        client.run()
