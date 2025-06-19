from openpyxl.cell import Cell

from issue_classes.abstract_issue import Handler

class NameIssue(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: tuple[Cell, Cell, Cell, Cell, Cell, Cell])-> bool:
        if request[0].internal_value == 'Имя':
            return super().handle(request)
        else:
            print( f'Неверное имя столбца "Имя" ({request})')
            return False
            