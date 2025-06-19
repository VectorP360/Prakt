from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class AbstractHandler(ABC):

    @abstractmethod
    def set_next(self, handler: AbstractHandler) -> AbstractHandler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class Handler(AbstractHandler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return True