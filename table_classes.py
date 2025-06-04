class Posts:
    def __init__(self, post_ID: int, post_name: str):
        self.post_ID = post_ID
        self.post_name = post_name

class Facility_types:
    def __init__(self, type_ID: int, type_name: str):
        self.type_ID = type_ID
        self.type_name = type_name

class SCADA_scheme:
    def __init__(self,scheme_ID: int, scheme_name: str):
        self.scheme_ID = scheme_ID
        self.scheme_name = scheme_name


class Facility:
    def __init__(self, facility_ID:int, type_ID:int, workshop_ID:int, scada_schema:int):
        self.facility_ID = facility_ID
        self.type_ID = type_ID
        self.workshop_ID = workshop_ID
        self.scada_schema = scada_schema


class Employee:
    def __init__(self, employee_ID:int, surname:str, name:str, fathersname:str, facility:Facility, post_ID:int, hire_date:str, employee_login:str, employee_password:str):
        self.employee_ID = employee_ID
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.facility = facility
        self.post_ID = post_ID
        self.hire_date = hire_date
        self.employee_login = employee_login
        self.employee_password = employee_password
