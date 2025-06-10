
from repository.repository import RepositoryManager

from client import TerminalClient

# Это твоя точка входа в программу
if __name__ == "main":
    
    manager = RepositoryManager()
    
    # Дописать класс TerminalClient таким образом, чтобы он принимал на вход только менеджер репозиториев
    client = TerminalClient(manager)
    client.run()
    