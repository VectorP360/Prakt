from issue_classes.abstract_issue import Handler

class FathresnameIssue(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request)-> str:
        if request[2].internal_value == 'Отчество':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Отчество" ({request})')
            return False