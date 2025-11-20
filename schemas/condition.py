from schemas.facility import FacilityOut


class ConditionsOut:
    def __init__(
        self,
        condition_id: int,
        temperature: int,
        loading: int,
        pressure: int,
        facility: FacilityOut,
    ):
        self.condition_id = condition_id
        self.temperature = temperature
        self.loading = loading
        self.pressure = pressure
        self.facility = facility

    def __str__(self):
        return f"""
        Установка = {self.facility.name}
        Температура (Цельсий) = {self.temperature}, 
        Нагрузка % = {self.loading},
        Давление = {self.pressure}
        """


class ConditionsIn:
    def __init__(
        self, temperature: int, loading: int, pressure: int, facility: FacilityOut
    ):
        self.temperature = temperature
        self.loading = loading
        self.pressure = pressure
        self.facility = facility
