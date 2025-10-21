from psycopg import connect

from repository.repository import RepositoryManager
from clients.user_terminal_client import UserTerminalClient
from clients.scada_terminal_client import ScadaTerminalClient
from clients.leader_choice_client import LeaderClient
from enums.posts import UserPost
from enums.clients import Clients

from tools.sing_up import SingUp

# Это точка входа в программу
if __name__ == "__main__":
    
    connection = connect(
        dbname = '',
        host = '',
        user = '',
        password = '',
        port = ''
        )
    
    manager = RepositoryManager(connection)

    user = SingUp(manager).singing_up()

    if user:
        match user.post.name:

            case UserPost.FIRST_CATEGORY.value:
                client = ScadaTerminalClient(manager = manager)
                client.get_scada_by_user(user_id = user.user_id)
        
            case UserPost.SENIOR.value:
                client = UserTerminalClient(manager = manager)
                client.run()

            case UserPost.MAIN_EXPERT.value:
                client = LeaderClient(manager = manager).run()
                if client:
                    client.run()
            
            case UserPost.DIRECTOR.value:
                client = LeaderClient(manager = manager).run()
                if client:
                    client.run()
    
    print('Программа завершена')