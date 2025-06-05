import facility
import posts

class Employee:
    def __init__(self, employee_ID:int, surname:str, name:str, fathersname:str, facility:facility.Facility, post: posts.Posts, hire_date:str, employee_login:str, employee_password:str):
        self.employee_ID = employee_ID
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.facility = facility
        self.post = post
        self.hire_date = hire_date
        self.employee_login = employee_login
        self.employee_password = employee_password
