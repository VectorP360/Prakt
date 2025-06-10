from schemas.facility_types import FacilityTypeOut
from schemas.workshop import WorkshopOut
from schemas.scada_scheme import ScadaSchemeOut

class FacilityOut:
    def __init__(self, facility_id: int, name: str, type: FacilityTypeOut, workshop: WorkshopOut, scada_scheme: ScadaSchemeOut):
        self.facility_id = facility_id
        self.name = name
        self.type = type
        self.workshop = workshop
        self.scada_scheme = scada_scheme

class FacilityIn:
    def __init__(self, name: str, type: FacilityTypeOut, workshop: WorkshopOut, scada_scheme: ScadaSchemeOut):
        self.name = name
        self.type = type
        self.workshop = workshop
        self.scada_scheme = scada_scheme