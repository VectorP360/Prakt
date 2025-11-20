from typing import Tuple
from openpyxl.cell import (
    Cell,
)  # , _CellOrMergedCell при импорте вызывает ошибку. Почему - Я не понял

from handlers.abstract_handler import Handler


class NowPostHandler(Handler):
    CHECKING_ROW = 3
    COLUMN_NAME = "Текущая должность"

    def handle(self, row: Tuple[Cell, ...]) -> bool:
        cell: Cell = row[self.CHECKING_ROW]

        if isinstance(cell, Cell) and cell.internal_value == self.COLUMN_NAME:
            return super().handle(row)
        else:
            print(f'Неверное имя столбца "{self.COLUMN_NAME}" ({row})')
            return False
