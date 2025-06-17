from enum import IntEnum, StrEnum

class NumChoice(IntEnum):

    create_user = 1
    select_user = 2
    edit_user = 3
    delete_user = 4
    exit_programm = 0

    select_id = 1
    select_all_users = 2

    new_hire_user = 1
    old_hire_user = 2

class StrChoice(StrEnum):
    gendir_post = 'Генеральный директор' 
    glavspec_post = 'Главный специалист'
    starspec_post = 'Старший специалист'
    spec1categ_post = 'Специалист 1 категории'
    