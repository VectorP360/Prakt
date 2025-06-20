from openpyxl.cell import Cell

from handlers.abstract_handler import Handler

class SurnameHandler(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[1].internal_value == 'Фамилия':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Фамилия" ({request})')
            return False