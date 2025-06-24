from typing import Tuple
from datetime import date

from openpyxl.cell import Cell#, _CellOrMergedCell при импорте вызывает ошибку. Почему - Я не понял

from handlers.abstract_handler import Handler

class TypeHireDateHandler(Handler):
    CHECKING_ROW = 3
    COLUMN_TYPE = 'date'
    
    def handle(self, row: Tuple[Cell, ...])-> bool:
        cell : Cell = row[self.CHECKING_ROW]
        
        if isinstance(cell.internal_value, date) :
            return super().handle(row)
        elif cell.internal_value == 'сегодня':
            return super().handle(row)
        else:
            print(f'Неверный тип данных ячейки "{cell.coordinate}" (Ожидалась дата)')
            return False
        
