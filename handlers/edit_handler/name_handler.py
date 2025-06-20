from typing import Tuple
from openpyxl.cell import _CellOrMergedCell, Cell

from handlers.abstract_handler import Handler


class NameHandler(Handler):
    CHECKING_ROW = 0
    COLUMN_NAME = "Имя"
    
    def handle(self, row: Tuple[_CellOrMergedCell, ...])-> bool:
        cell: _CellOrMergedCell = row[self.CHECKING_ROW]
        
        if isinstance(cell, Cell) and cell.internal_value == self.COLUMN_NAME:
            return super().handle(row)
        else:
            print(f'Неверное имя столбца "{self.COLUMN_NAME}" ({row})')
            return False
            