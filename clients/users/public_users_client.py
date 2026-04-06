from typing import TypedDict
from requests import Response
from clients.api_client import APIClient


class UserRequestData(TypedDict):
    """
        Структура формирования данных запроса метода POST
    """
    username: str
    email: str
    password: str


class PublicUsersClient(APIClient):
    """
        Клиент для работы с публичными методами API пользователей.
    """
    def create_user_api(self, request: UserRequestData) -> Response:
        """
            Выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя.
            :param request: Словарь с данными (username, email, password),
                               соответствующий структуре UserCreateRequest.
            :return: Объект httpx.Response с данными ответа от сервера.
        """
        return self.post("/api/v1/users", json=request)
