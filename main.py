from psycopg import connect

from repository.repository import RepositoryManager
from client import TerminalClient

# Это твоя точка входа в программу (Почему-то не работает)
if __name__ == "main":
    manager = RepositoryManager(connection = connect(
        dbname = '',
        host = '',
        user = '',
        password = '',
        port = ''
        )
    )
        
        # Дописать класс TerminalClient таким образом, чтобы он принимал на вход только менеджер репозиториев
    client = TerminalClient(manager)
    client.run()