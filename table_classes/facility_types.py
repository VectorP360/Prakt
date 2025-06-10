class FacilityTypeOut:
    def __init__(self, facility_type_ID: int, facility_type_name: str):
        self.facility_type_ID = facility_type_ID
        self.facility_type_name = facility_type_name

class FacilityTypeIn:
    def __init__(self, facility_type_name: str):
        self.facility_type_name = facility_type_name