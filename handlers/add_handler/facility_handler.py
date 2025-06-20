from openpyxl.cell import Cell

from handlers.abstract_handler import Handler


class FacilityHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[5].internal_value == 'Установка':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Установка" ({request})')
            return False
