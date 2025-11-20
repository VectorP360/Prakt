from schemas.facility import FacilityOut
from schemas.element_type import ElementTypeOut


class ElementOut:
    def __init__(
        self,
        element_id: int,
        name: str,
        material: str,
        element_type: ElementTypeOut,
        facility: FacilityOut,
    ):
        self.element_id = element_id
        self.name = name
        self.material = material
        self.element_type = element_type
        self.facility = facility

    def __str__(self):
        return f"""
        ID = {self.element_id}, название: {self.name}
        материал = {self.material}, тип элемента = {self.element_type.name}
        установка = {self.facility.name}\n"""


class ElementIn:
    def __init__(
        self,
        name: str,
        material: str,
        element_type: ElementTypeOut,
        facility: FacilityOut,
    ):
        self.name = name
        self.material = material
        self.element_type = element_type
        self.facility = facility
