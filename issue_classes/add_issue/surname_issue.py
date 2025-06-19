from issue_classes.abstract_issue import Handler

class SurnameIssue(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request)-> str:
        if request[1].internal_value == 'Фамилия':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Фамилия" ({request})')
            return False