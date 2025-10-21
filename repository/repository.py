from psycopg import Connection

from . import (
    WorkshopRepository, 
    UserRepository, 
    ScadaSchemeRepository, 
    PostsRepository, 
    FacilityTypesRepository, 
    FacilityRepository
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
    
    def get_posts_repository(self):
        return PostsRepository(self._connection)
    
    def get_facility_types_repository(self):
        return FacilityTypesRepository(self._connection)
    
    def get_facility_repository(self):
        return FacilityRepository(self._connection)