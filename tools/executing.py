from repository.repository import RepositoryManager

from clients.user_terminal_client import UserTerminalClient
from clients.scada_terminal_client import ScadaTerminalClient
from clients.leader_choice_client import LeaderClient
from  clients.worker_client import WorkerClient

from enums.posts import UserPost

from tools.sing_up import SingUp

class Executer():
    def __init__(self, manager: RepositoryManager):
        self.manager = manager

    def execute(self):
        user = SingUp(self.manager).singing_up()

        if user:
            match user.post.name:

                case UserPost.FIRST_CATEGORY.value:
                    client = WorkerClient(manager = self.manager, user = user)
                    client.run()
            
                case UserPost.SENIOR.value:
                    client = UserTerminalClient(manager = self.manager)
                    client.run()

                case UserPost.MAIN_EXPERT.value:
                    client = LeaderClient(manager = self.manager).run()
                    if client:
                        client.run()
                
                case UserPost.DIRECTOR.value:
                    client = LeaderClient(manager = self.manager).run()
                    if client:
                        client.run()