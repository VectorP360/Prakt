from openpyxl.cell import Cell

from handlers.abstract_handler import Handler

class NewPostHandler(Handler):
    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[4].internal_value == 'Новая должность':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Новая должность" ({request})')
            return False