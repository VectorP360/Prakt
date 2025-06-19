from issue_classes.abstract_issue import Handler

class HireDateIssue(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request)-> str:
        if request[3].internal_value == 'Дата найма':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Дата найма" ({request})')
            return False    