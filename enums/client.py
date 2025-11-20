from enum import Enum

class Client(Enum):
    SCADA = 'scada_terminal_client.py'
    USER = 'user_terminal_client.py'
    
    ALL = [SCADA, USER]