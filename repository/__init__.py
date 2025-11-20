from .facility_repository import FacilityRepository
from .facility_types_repository import FacilityTypesRepository
from .posts_repository import PostsRepository
from .scada_repository import ScadaSchemeRepository
from .user_repository import UserRepository
from .workshop_repository import WorkshopRepository
from .element_types_repository import ElementTypesRepository
from .element_repository import ElementRepository
# from .repository import RepositoryManager

# При использовании программы, она начинает жаловаться на circular import.
# Жаловалось на импорт 6-ти классов-репозиториев в файте repository.py
# После комментирывания строки 4, ошибка перестала возникать

__all__ = [
    "FacilityRepository",
    "FacilityTypesRepository",
    "PostsRepository",
    "ScadaSchemeRepository",
    "UserRepository",
    "WorkshopRepository",
    "ElementTypesRepository",
    "ElementRepository",
    # "RepositoryManager" # Эту строку я закомментирывал так, на всякий
]
