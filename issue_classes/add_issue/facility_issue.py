from issue_classes.abstract_issue import Handler

class FacilityIssue(Handler):

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request)-> str:
        if request[5].internal_value == 'Установка':
            return super().handle(request)
        else:
            print(f'Неверное имя столбца "Установка" ({request})')
            return False