from src.repositories.repository import RepositoryManager

from src.clients.user_terminal_client import UserTerminalClient
from src.clients.leader_choice_client import LeaderClient
from src.clients.worker_client import WorkerClient
from src.enums.post import UserPost
from src.tools.sing_up import SingUp


class Executer:
    def __init__(self, manager: RepositoryManager):
        self.manager = manager

    def execute(self):
        user = SingUp(self.manager).singing_up()

        if user:
            match user.post.name:
                case UserPost.FIRST_CATEGORY.value:
                    client = WorkerClient(manager=self.manager, user=user)
                    client.run()

                case UserPost.SENIOR.value:
                    client = UserTerminalClient(manager=self.manager)
                    client.run()

                case UserPost.MAIN_EXPERT.value:
                    client = LeaderClient(manager=self.manager).run()
                    if client:
                        client.run()

                case UserPost.DIRECTOR.value:
                    client = LeaderClient(manager=self.manager).run()
                    if client:
                        client.run()
