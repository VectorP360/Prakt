import workshop

class InnerStorageWorkshopRepository:
    def __init__(self, storage: dict[int, workshop.Workshop]):
        self.storage = storage

    def create(self, workshop_id: int, workshop_name: str):

        #создать объект класса Workshop
        #Передать в storage ключ (значение Workshop.workhsop_ID) и сам объект Workshop

        new_workshop = workshop.Workshop(workshop_id, workshop_name)
        self.storage[workshop_id] = new_workshop

    def get_by_ID(self, workshop_id):

        #Вернуть значение (объект) по введённому workshop_ID

        return self.storage.get(workshop_id)
    
    def get_all(self):
        
        #создать список из атрибутов (workshop_name) объектов 
        #вернуть все значениЯ (объектЫ)
        workshop_objects = self.storage.values()
        workshop_names = []

        for iteration_name in workshop_objects:
            workshop_names.append(iteration_name.workshop_name)

        return workshop_names

    def update(self, workshop_id, new_name):

        #при помощи метода get_by_ID нужный объект класса Workshop
        
        self.storage[workshop_id].workshop_name = new_name

    def delete(self, workshop_id: int):

        #Вызывается методо pop у записи в словаре с указанным workshop_id

        self.storage.pop(workshop_id)

workshop_repo = InnerStorageWorkshopRepository(storage={})

workshop_repo.create(1, 'Цех 1')
print(workshop_repo.get_by_ID(1).workshop_name)

workshop_repo.create(2,'Цех 2')
print(workshop_repo.get_by_ID(2).workshop_name)

workshop_repo.update(1,'Цех 3')

workshop_repo.delete(2)

print((workshop_repo.get_all()))