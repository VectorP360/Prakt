from typing import Optional

from repository.user_repository import EmployeeRepository, EmployeeOut
from repository.facility_repository import FacilityRepository, FacilityOut
from repository.posts_repository import PostsRepository, PostsOut

def list_for_employees(employee_repo: EmployeeRepository) -> Optional[EmployeeOut]:
    employees = []
    iteration_number = 0

    for iteration in employee_repo.get_all():
        print(f'''Сотрудник №{iteration_number}: ФИО: {iteration.surname} {iteration.name} {iteration.fathersname}, установка: {iteration.facility.name}, должность: {iteration.post.post_name}''')
        employees.append(iteration.employee_id)
        iteration_number += 1

    edit_employee = int(input('\nВведите номер сотрудника, чью запись хотите изменить: '))

    try:
        return employee_repo.get_by_ID(employees[edit_employee])
    except IndexError:
        return


def list_for_facilityes(facility_repo: FacilityRepository) -> Optional[FacilityOut]:
    facilityes = []
    iteration_number = 0 

    print('\nУстановки:')
    for iteration in facility_repo.get_all():
        print(f'''Установка №: {iteration_number}: Наименование: {iteration.name}, {iteration.type.facility_type_name}, {iteration.workshop.name}, {iteration.scada_scheme.scheme_name}''')
        facilityes.append(iteration.facility_id)
        iteration_number += 1

    facility_id = int(input('На какой установке (номер установки) будет работать сотрудник?: '))

    try:
        return facility_repo.get_by_ID(facilityes[facility_id])
    except IndexError:
        return
    

def list_for_posts(posts_repo: PostsRepository) -> Optional[PostsOut]:
    posts = []
    iteration_number = 0

    print('\nДолжности:')
    for iteration in posts_repo.get_all():
        print(f'''Должность №{iteration_number}: Наименование: {iteration.post_name}''')
        posts.append(iteration.post_ID)
        iteration_number += 1

    post = int(input('Должность сотрудника (Номер должности): '))

    try:
        return posts_repo.get_by_ID(posts[post])
    except IndexError:
        return