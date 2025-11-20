class FacilityTypeOut:
    def __init__(self, facility_type_id: int, name: str):
        self.facility_type_id = facility_type_id
        self.name = name

    def __str__(self):
        return f"id типа установок: {self.facility_type_id}, название: {self.name}"


class FacilityTypeIn:
    def __init__(self, name: str):
        self.name = name
