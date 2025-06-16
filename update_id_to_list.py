from typing import Optional

from repository.user_repository import UserRepository, UserOut
from repository.facility_repository import FacilityRepository, FacilityOut
from repository.posts_repository import PostsRepository, PostsOut

def list_for_users(user_repo: UserRepository) -> Optional[UserOut]:
    users = []
    iteration_number = 0

    for iteration in user_repo.get_all():
        print('Номер сотрудника: ',iteration_number,'\n',iteration)
        users.append(iteration.user_id)
        iteration_number += 1

    edit_user = int(input('\nВведите номер сотрудника, чью запись хотите изменить: '))

    try:
        return user_repo.get_by_ID(users[edit_user])
    except IndexError:
        return


def list_for_facilityes(facility_repo: FacilityRepository) -> Optional[FacilityOut]:
    facilityes = []
    iteration_number = 0 

    print('\nУстановки:')
    for iteration in facility_repo.get_all():
        print(f'Установка №{iteration_number} , {iteration}')
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
        print(f'Должность №{iteration_number}: Наименование: {iteration.name}')
        posts.append(iteration.post_ID)
        iteration_number += 1

    post = int(input('Должность сотрудника (Номер должности): '))

    try:
        return posts_repo.get_by_ID(posts[post])
    except IndexError:
        return