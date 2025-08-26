from psycopg import connect

from repository.repository import RepositoryManager
from clients.user_terminal_client import UserTerminalClient
from clients.scada_terminal_client import ScadaTerminalClient

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
        
    client = ScadaTerminalClient(manager)
    
    client.run()
    