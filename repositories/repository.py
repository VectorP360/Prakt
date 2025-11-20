from psycopg import Connection

from . import (
    WorkshopRepository,
    UserRepository,
    ScadaSchemeRepository,
    PostRepository,
    FacilityTypeRepository,
    FacilityRepository,
    ElementTypeRepository,
    ElementRepository,
    ConditionRepository,
)


class RepositoryManager:
    def __init__(self, connection: Connection):
        self._connection = connection

    def get_workshop_repository(self):
        return WorkshopRepository(self._connection)

    def get_user_repository(self):
        return UserRepository(self._connection)

    def get_scada_scheme_repository(self):
        return ScadaSchemeRepository(self._connection)

    def get_post_repository(self):
        return PostRepository(self._connection)

    def get_facility_types_repository(self):
        return FacilityTypeRepository(self._connection)

    def get_facility_repository(self):
        return FacilityRepository(self._connection)

    def get_element_types_repository(self):
        return ElementTypeRepository(self._connection)

    def get_element_repository(self):
        return ElementRepository(self._connection)

    def get_conditions_repository(self):
        return ConditionRepository(self._connection)
