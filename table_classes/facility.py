from table_classes.facility_types import FacilityTypesOut
from table_classes.workshop import WorkshopOut
from table_classes.scada_scheme import ScadaSchemeOut

class FacilityOut:
    def __init__(self, facility_id: int, name: str, type: FacilityTypesOut, workshop: WorkshopOut, scada_schema: ScadaSchemeOut):
        self.facility_id = facility_id
        self.name = name
        self.type = type
        self.workshop = workshop
        self.scada_scheme = scada_schema

class FacilityIn:
    def __init__(self, name: str, type: FacilityTypesOut, workshop: WorkshopOut, scada_schema: ScadaSchemeOut):
        self.name = name
        self.type = type
        self.workshop = workshop
        self.scada_schema = scada_schema