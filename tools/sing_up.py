from typing import Optional

from repositories.repository import RepositoryManager
from schemas.user import UserOut
from enums.acceptance import Acceptance


class SingUp:
    def __init__(self, repository_manager: RepositoryManager):
        self.repository_manager = repository_manager

    def singing_up(self) -> Optional[UserOut]:
        check = True

        while check:
            login = input(str("Пожалуйста, введите свой логин: "))
            password = input(str("Пожалуйста, введите пароль: "))

            logined_user = self.repository_manager.get_user_repository().get_by_login(
                login, password
            )

            if logined_user:
                return logined_user

            print("Неверный логин или пароль!\nХотите повторить попытку входа?")
            if (
                input("(y/n) если вы ничего не введёте, будет выбран вариант n: ")
                == Acceptance.YES
            ):
                pass
            else:
                return None
