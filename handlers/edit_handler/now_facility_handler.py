from openpyxl.cell import Cell

from handlers.abstract_handler import Handler

class NowFacilityHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[5].internal_value == 'Текущая установка':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Текущая установка" ({request})')
            return False