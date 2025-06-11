from psycopg import Connection

class RepositoryManager:
    def __init__(self, connection: Connection):
        self._connection = connection
    
    # TODO: Допиши в данном классе по методу, который бы возвращал объект своего класса репозитория
    # например, get_facility_repository(), который возвращает объект класса FacilityRepository. 
    # И так для всех классов. Чтобы через объект класса RepositoryManager можно было получить любой репозиторий.
    
    