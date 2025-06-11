from schemas.facility_types import FacilityTypeOut
from schemas.workshop import WorkshopOut

class FacilityOut:
    def __init__(self, facility_id: int, name: str, type: FacilityTypeOut, workshop: WorkshopOut):
        self.facility_id = facility_id
        self.name = name
        self.type = type
        self.workshop = workshop

class FacilityIn:
    def __init__(self, name: str, type: FacilityTypeOut, workshop: WorkshopOut):
        self.name = name
        self.type = type
        self.workshop = workshop