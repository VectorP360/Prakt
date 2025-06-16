from psycopg import Connection

from repository.workshop_repository import WorkshopRepository
from repository.user_repository import UserRepository
from repository.scada_repository import ScadaSchemeRepository
from repository.posts_repository import PostsRepository
from repository.facility_types_repository import FacilityTypesRepository
from repository.facility_repository import FacilityRepository

class RepositoryManager:
    def __init__(self, connection: Connection):
        self._connection = connection
    
    # TODO: Допиши в данном классе по методу, который бы возвращал объект своего класса репозитория
    # например, get_facility_repository(), который возвращает объект класса FacilityRepository. 
    # И так для всех классов. Чтобы через объект класса RepositoryManager можно было получить любой репозиторий.
    
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