from enum import Enum


class UserPost(Enum):
    DIRECTOR = "Генеральный директор"
    MAIN_EXPERT = "Главный специалист"
    SENIOR = "Старший специалист"
    FIRST_CATEGORY = "Специалист 1 категории"

    LEADERSHIP = [DIRECTOR, MAIN_EXPERT]
