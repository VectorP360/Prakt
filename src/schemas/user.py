from src.schemas.facility import FacilityOut
from src.schemas.post import PostOut


class UserOut:
    def __init__(
        self,
        user_id: int,
        surname: str,
        name: str,
        fathersname: str,
        facility: FacilityOut,
        post: PostOut,
        hire_date: str,
        login: str,
        password: str,
    ):
        self.user_id = user_id
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.hire_date = hire_date
        self.login = login
        self.password = password
        self.facility = facility
        self.post = post

    def __str__(self):
        return f"""
        ID {self.user_id}, 
        ФИО: {self.surname} {self.name} {self.fathersname}, 
        установка: {self.facility.name}, 
        должность: {self.post.name}, 
        Дата найма: {self.hire_date}, 
        Логин {self.login}\n"""


class UserIn:
    def __init__(
        self,
        surname: str,
        name: str,
        fathersname: str,
        facility: FacilityOut,
        post: PostOut,
        hire_date: str,
        login: str,
        password: str,
    ):
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.hire_date = hire_date
        self.login = login
        self.password = password
        self.facility = facility
        self.post = post
