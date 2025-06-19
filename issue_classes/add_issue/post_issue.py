from issue_classes.abstract_issue import Handler

class PostIssue(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request)-> str:
        if request[4].internal_value == 'Должность':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Должность" ({request})')
            return False