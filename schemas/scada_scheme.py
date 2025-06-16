from schemas.facility import FacilityOut

class ScadaSchemeOut:
    def __init__(self,scheme_id: int, name: str, facility: FacilityOut):
        self.scheme_id = scheme_id
        self.name = name
        self.facility = facility

    def __str__(self):
        return f'id схемы: {self.scheme_id}, название: {self.name}, установка: {self.facility.name}'

class ScadaSchemeIn:
    def __init__(self, name: str, facility: FacilityOut):
        self.name = name
        self.facility = facility