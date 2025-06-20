from openpyxl.cell import Cell

from handlers.abstract_handler import Handler

class NowPostHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[3].internal_value == 'Текущая должность':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Текущая должность" ({request})')
            return False