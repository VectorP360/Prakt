class WorkshopOut:
    def __init__(self, workshop_id: int, name: str):
        self.workshop_id = workshop_id
        self.name = name

    def __str__(self):
        return f'id цеха: {self.workshop_id}, название цеха: {self.name}'

class WorkshopIn:
    def __init__(self,name: str):
        self.name = name