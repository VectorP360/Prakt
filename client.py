from datetime import datetime

from repository_classes.employee_repository import EmployeeRepository, EmployeeIn
from repository_classes.facility_repository import FacilityRepository
from repository_classes.posts_repository import PostsRepository

# коректная обработка даты, возможность пользователя выходить из любого этапа на стартовый
# Дать пользователю возможность выбирать не id , а порядковый номер в выводимом списке.

class UserClass:
    def __init__(self, employee_repo: EmployeeRepository, posts_repo: PostsRepository, facility_repo: FacilityRepository):
        self.employee_repo = employee_repo
        self.posts_repo = posts_repo
        self.facility_repo = facility_repo

    def insert(self):
        
        print('Для создания записи о сотруднике укажите все перечисленные данные:')
        surname = str(input('Фамилия: '))
        name = str(input('Имя: '))
        fathersname = str(input('Отчество: '))

        print('\nУстановки:')
            
        for iteration in self.facility_repo.get_all():
            print(f'''ID: {iteration.facility_id}, Наименование: {iteration.name}, {iteration.type.facility_type_name}, {iteration.workshop.name}, {iteration.scada_scheme.scheme_name}''')
                
        facility = int(input('На какой установке (ID установки) будет работать сотрудник: '))

        print('\nДолжности:')
        for iteration in self.posts_repo.get_all():
            print(f'''ID: {iteration.post_ID}, Наименование: {iteration.post_name}''')

        post = int(input('Должность сотрудника (ID должности): '))

        new_hire = int(input('\nЭто новый сотрудник, или старый, которого ещё нет в базе данных?\n1: Новый сотрудник\n2: Старый сотрудник\n'))
        if new_hire == 1:
            hire_date = datetime.today()
        elif new_hire == 2:
            hire_date = (input('Дата найма сотрудника (год-месяц-число): '))

        employee_login = str(input('Логин сотрудника: '))
        employee_password = str(input('Личный пароль сотруднка: '))

        facility_in = self.facility_repo.get_by_ID(facility)
        post_in = self.posts_repo.get_by_ID(post)

        new_employee = self.employee_repo.create(new_employee = EmployeeIn(surname, name, fathersname, facility = facility_in, post = post_in, 
                                                                    hire_date = hire_date, employee_login = employee_login, employee_password = employee_password))

        print(f'''ID {new_employee.employee_id}, ФИО: {new_employee.surname} {new_employee.name} {new_employee.fathersname}, установка: {new_employee.facility.name}, должность: {new_employee.post.post_name}, Дата найма: {new_employee.hire_date}, Логин {new_employee.employee_login}''')
            
        input('Нажмите Enter что бы продолжить ')


    def select(self):
        select_type = input('Вы хотите просмотреть одну запись с конкретным ID или сразу все?\n1: C конкретным ID\n2: Все записи\n')

        if select_type == '1':
            needed_ID = input('Введите ID записи которую хотите просмотреть\n')
            founded_employee = self.employee_repo.get_by_ID(needed_ID)
            if founded_employee:
                print(f'''ID {founded_employee.employee_id}, ФИО: {founded_employee.surname} {founded_employee.name} {founded_employee.fathersname}, Установка: {founded_employee.facility.name}, Должность: {founded_employee.post.post_name}, Дата найма {founded_employee.hire_date}, Логин {founded_employee.employee_login}''')
            else:
                print('Записи с указанным ID не найдено')
            input('Нажмите Enter что бы продолжить ')
            
        elif select_type == '2':
            for founded_employee in (self.employee_repo.get_all()):
                print(f'''ID {founded_employee.employee_id}, ФИО: {founded_employee.surname} {founded_employee.name} {founded_employee.fathersname}, Установка: {founded_employee.facility.name}, Должность: {founded_employee.post.post_name}, Дата найма {founded_employee.hire_date}, Логин {founded_employee.employee_login}''')
            input('Нажмите Enter что бы продолжить ')


    def update(self):

        for iteration in self.employee_repo.get_all():
            print(f'''ID: {iteration.employee_id}, ФИО: {iteration.surname} {iteration.name} {iteration.fathersname}, должность: {iteration.post.post_name}''')
        
        edit_employee = int(input('Введите ID сотрудника, чью запись хотите изменить: '))
        
        if self.employee_repo.get_by_ID(edit_employee):
            
            surname = str(input('Новая фамилия: '))
            name = str(input('Новое имя: '))
            fathersname = str(input('Новое отчество: '))

            print('\nУстановки:')
            
            for iteration in self.facility_repo.get_all():
                print(f'''ID: {iteration.facility_id}, Наименование: {iteration.name}, {iteration.type.facility_type_name}, {iteration.workshop.name}, {iteration.scada_scheme.scheme_name}''')
                    
            facility_id = int(input('На какой установке (ID установки) будет работать сотрудник: '))

            if self.facility_repo.get_by_ID(facility_id):

                print('\nДолжности:')
                for iteration in self.posts_repo.get_all():
                    print(f'''ID: {iteration.post_ID}, Наименование: {iteration.post_name}''')

                post = int(input('Должность сотрудника (ID должности): '))

                if self.posts_repo.get_by_ID(post):
                    
                    new_hire = int(input('\nЭто новый сотрудник, или старый, которого ещё нет в базе данных?\n1: Новый сотрудник\n2: Старый сотрудник\n'))
                    if new_hire == 1:
                        hire_date = datetime.today()
                    elif new_hire == 2:
                        hire_date = int(input('Дата найма сотрудника (год-месяц-число): '))
                    employee_login = str(input('Новый логин сотрудника: '))
                    employee_password = str(input('Новый личный пароль сотруднка: '))

                    facility_in = self.facility_repo.get_by_ID(facility_id)
                    post_in = self.posts_repo.get_by_ID(post)

                    upd_employee = self.employee_repo.update(edit_employee, new_employee = EmployeeIn(surname, name, fathersname, facility_in, post_in, hire_date, employee_login, employee_password))

                    print(f'''ID {upd_employee.employee_id}, ФИО: {upd_employee.surname} {upd_employee.name} {upd_employee.fathersname}, установка: {upd_employee.facility.name}, должность: {upd_employee.post.post_name}, Дата найма: {upd_employee.hire_date}, Логин {upd_employee.employee_login}''')
                else:
                    print('Должности с указанным ID не обнаружено')
            else:
                print('Установки с указанным ID не обнаружено')
        else:
            print('Сотрудника с данным ID не обнаружено')
        input('Нажмите Enter что бы продолжить')


    def delete(self):
                
        print('\nСотрудники:')
        for iteration in self.employee_repo.get_all():
            print(f'''ID: {iteration.employee_id}, ФИО: {iteration.surname} {iteration.name} {iteration.fathersname}, должность: {iteration.post.post_name}''')
            
        deleted_employee = input('Введите ID сотрудника, чью запись хотите удалить: ')
        acception = input('\nВы уверенны, что хотите удалить эту запись? \nПосле удаления её нельзя будет восстановить (y/n): ')

        if acception == 'y':
            check = self.employee_repo.delete(deleted_employee)
            if check:
                print('Удаление произшло успешно!')
                input('Нажмите Enter что бы продолжить')
            else:
                print('Удаление не состоялось!')
                input('Нажмите Enter что бы продолжить')