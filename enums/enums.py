from enum import IntEnum, StrEnum, Enum


class Command(IntEnum):
    CREATE_USER = 1
    SELECT_USER = 2
    UPDATE_USER = 3
    DELETE_USER = 4
    EDIT_BY_EXEL = 5
    CREATE_BY_EXCEL = 6
    EXIT = 0

    SHOW_USER_BY_ID = 1
    SHOW_ALL_USERS = 2

    NEW_HIRE_USER = 1
    OLD_HIRE_USER = 2


class UserPost(Enum):
    DIRECTOR = 'Генеральный директор' 
    MAIN_EXPERT = 'Главный специалист'
    SENIOR = 'Старший специалист'
    FIRST_CATEGORY = 'Специалист 1 категории'
    
    LEADERSHIP = [DIRECTOR, MAIN_EXPERT]
    
    
class Acceptance(StrEnum):
    YES = "y"
    NO = "n"
