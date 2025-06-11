from schemas.facility import FacilityOut, FacilityTypeOut, WorkshopOut, ScadaSchemeOut
from schemas.posts import PostsOut

class UserOut:
    def __init__(self, user_id: int, surname:str, name:str, fathersname:str, facility:FacilityOut, post: PostsOut, hire_date:str, login:str, password:str):
        self.user_id = user_id
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.hire_date = hire_date
        self.login = login
        self.password = password
        self.facility = facility
        self.post = post

class UserIn:
    def __init__(self, surname:str, name:str, fathersname:str, facility:FacilityOut, post: PostsOut, hire_date:str, login:str, password:str):
        self.surname = surname
        self.name = name
        self.fathersname = fathersname
        self.hire_date = hire_date
        self.login = login
        self.password = password
        self.facility = facility
        self.post = post
