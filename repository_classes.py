import table_classes

class WorkshopRepository:
    def __init__(self, workshop_id: int):
        self.__workshop_id: int = workshop_id
        self.__workshop_name: str = 'Цех №'+ str(self.__workshop_id)
        self.__used_id = {}

    @property
    def workshop_id(self):
        return self.__workshop_id
    
    @workshop_id.setter
    def workshop_id(self, new_id):
        self.__workshop_id = new_id

    def create(self):

        if self.__used_id.get(self.__workshop_id):
            print('Элемент с данным ID уже существует')

        new_workshop = table_classes.Workshop(self.__workshop_id, self.__workshop_name)
        self.__used_id[self.__workshop_id] = new_workshop

    def read(self, workshop_id):

        workshop = self.__used_id.get(workshop_id)
        return workshop

    def update(self, workshop_id, new_id):

        if new_id not in self.__used_id.keys() and workshop_id in self.__used_id:
            workshop = self.__used_id.get(workshop_id)
        workshop.workshop_ID = new_id
        self.__used_id[new_id] = workshop

    def delete(self):
        if self.__used_id.get(self.__workshop_id):
            self.__used_id.pop(self.__workshop_id)
        else:
            print('Записи с данным ID не существует')