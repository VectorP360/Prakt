from .facility_repository import FacilityRepository
from .facility_type_repository import FacilityTypeRepository
from .post_repository import PostRepository
from .scada_repository import ScadaSchemeRepository
from .user_repository import UserRepository
from .workshop_repository import WorkshopRepository
from .element_type_repository import ElementTypeRepository
from .element_repository import ElementRepository
from .condition_repository import ConditionRepository
from .operation_repository import OperationRepository
from .log_repository import LogRepository
# from .repository import RepositoryManager

# При использовании программы, она начинает жаловаться на circular import.
# Жаловалось на импорт 6-ти классов-репозиториев в файте repository.py
# После комментирывания строки 4, ошибка перестала возникать

__all__ = [
    "FacilityRepository",
    "FacilityTypeRepository",
    "PostRepository",
    "ScadaSchemeRepository",
    "UserRepository",
    "WorkshopRepository",
    "ElementTypeRepository",
    "ElementRepository",
    "ConditionRepository",
    "OperationRepository",
    "LogRepository",
    # "RepositoryManager" # Эту строку я закомментирывал так, на всякий
]
