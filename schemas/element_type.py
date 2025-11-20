class ElementTypeOut:
    def __init__(self, element_type_id: int, name: str):
        self.element_type_id = element_type_id
        self.name = name

    def __str__(self):
        return f'id типа установок: {self.element_type_id}, название: {self.name}'

class ElementTypeIn:
    def __init__(self, name: str):
        self.name = name