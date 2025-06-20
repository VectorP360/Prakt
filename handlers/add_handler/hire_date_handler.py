from openpyxl.cell import Cell

from handlers.abstract_handler import Handler


class HireDateHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[3].internal_value == 'Дата найма':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Дата найма" ({request})')
            return False
        
