from psycopg import connect

from repository.repository import RepositoryManager
from clients.terminal_client import TerminalClient

# Это точка входа в программу
if __name__ == "main":
    
    connection = connect(
        dbname = '',
        host = '',
        user = '',
        password = '',
        port = ''
        )
    
    manager = RepositoryManager(connection)
        
    client = TerminalClient(manager)
    
    client.run()
    