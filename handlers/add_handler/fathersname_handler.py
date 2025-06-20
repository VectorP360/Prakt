from openpyxl.cell import Cell

from handlers.abstract_handler import Handler


class FathresnameHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[2].internal_value == 'Отчество':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Отчество" ({request})')
            return False
