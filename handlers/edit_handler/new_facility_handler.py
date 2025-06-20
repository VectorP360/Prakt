from openpyxl.cell import Cell

from handlers.abstract_handler import Handler

class NewFacilityHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[6].internal_value == 'Новая установка':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Новая установка" ({request})')
            return False