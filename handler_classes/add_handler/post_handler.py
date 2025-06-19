from openpyxl.cell import Cell

from handler_classes.abstract_handler import Handler

class PostHandler(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[4].internal_value == 'Должность':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Должность" ({request})')
            return False