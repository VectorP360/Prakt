from openpyxl.cell import Cell

from handlers.abstract_handler import Handler


class PostHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[4].internal_value == 'Должность':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Должность" ({request})')
            return False
