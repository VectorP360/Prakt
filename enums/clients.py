from enum import Enum

class Clients(Enum):
    SCADA = 'scada_terminal_client.py'
    USER = 'user_terminal_client.py'
    
    ALL = [SCADA, USER]