from schemas.facility_types import FacilityTypeOut
from schemas.workshop import WorkshopOut

class FacilityOut:
    def __init__(self, facility_id: int, name: str, type: FacilityTypeOut, workshop: WorkshopOut):
        self.facility_id = facility_id
        self.name = name
        self.type = type
        self.workshop = workshop

    def __str__(self):
        return f'id установки {self.facility_id}, установка {self.name}, тип: {self.type.name}, цех: {self.workshop.name}'

class FacilityIn:
    def __init__(self, name: str, type: FacilityTypeOut, workshop: WorkshopOut):
        self.name = name
        self.type = type
        self.workshop = workshop