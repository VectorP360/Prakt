from table_classes.facility import FacilityOut, FacilityTypesOut, WorkshopOut, ScadaSchemeOut
from table_classes.posts import PostsOut

class EmployeeOut:
    def __init__(self, employee_id: int, surname:str, name:str, fathersname:str, facility:FacilityOut, post: PostsOut, hire_date:str, employee_login:str, employee_password:str):
        self.employee_id = employee_id
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.facility = facility
        self.post = post
        self.hire_date = hire_date
        self.employee_login = employee_login
        self.employee_password = employee_password

class EmployeeIn:
    def __init__(self, surname:str, name:str, fathersname:str, facility:FacilityOut, post: PostsOut, hire_date:str, employee_login:str, employee_password:str):
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.facility = facility
        self.post = post
        self.hire_date = hire_date
        self.employee_login = employee_login
        self.employee_password = employee_password
