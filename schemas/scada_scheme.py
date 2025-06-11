from schemas.facility import FacilityOut

class ScadaSchemeOut:
    def __init__(self,scheme_id: int, name: str, facility: FacilityOut):
        self.scheme_id = scheme_id
        self.name = name
        self.facility = facility

class ScadaSchemeIn:
    def __init__(self, name: str, facility: FacilityOut):
        self.name = name
        self.facility = facility