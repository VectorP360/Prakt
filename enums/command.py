from enum import IntEnum

class Command(IntEnum):
    CREATE_USER = 1
    SELECT_USER = 2
    UPDATE_USER = 3
    DELETE_USER = 4
    EDIT_BY_EXEL = 5
    CREATE_BY_EXCEL = 6
    EXIT = 0

    SHOW_BY_ID = 1
    SHOW_ALL = 2

    NEW_HIRE_USER = 1
    OLD_HIRE_USER = 2

    CREATE_SCADA = 1
    SELECT_SCADA = 2
    UPDATE_SCADA = 3
    DELETE_SCADA = 4
    SHOW_SCADA_USER = 5