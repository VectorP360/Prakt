class ScadaSchemeOut:
    def __init__(self,scheme_ID: int, scheme_name: str):
        self.scheme_ID = scheme_ID
        self.scheme_name = scheme_name

class ScadaSchemeIn:
    def __init__(self, scheme_name: str):
        self.scheme_name = scheme_name