from typing import Tuple
from openpyxl.cell import (
    Cell,
)  # , _CellOrMergedCell при импорте вызывает ошибку. Почему - Я не понял

from src.handlers.abstract_handler import Handler


class TypeSurnameHandler(Handler):
    CHECKING_ROW = 1
    COLUMN_TYPE = "str"

    def handle(self, row: Tuple[Cell, ...]) -> bool:
        cell: Cell = row[self.CHECKING_ROW]

        if isinstance(cell.internal_value, str):
            return super().handle(row)
        else:
            print(f'Неверный тип данных "{cell.coordinate}" (Ожидалась строка)')
            return False
