from typing import TypedDict

from requests import Response

from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class CreateUserRequestDict(TypedDict):
    """
        Структура формирования данных запроса метода POST
    """
    username: str
    email: str
    password: str

# Добавили описание структуры пользователя
class User(TypedDict):
    """
    Описание структуры пользователя.
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

# Добавили описание структуры ответа создания пользователя
class CreateUserResponseDict(TypedDict):
    """
    Описание структуры ответа создания пользователя.
    """
    user: User

class PublicUsersClient(APIClient):
    """
        Клиент для работы с публичными методами API пользователей.
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
            Выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя.
            :param request: Словарь с данными (username, email, password),
                               соответствующий структуре UserCreateRequest.
            :return: Объект httpx.Response с данными ответа от сервера.
        """
        return self.post("/api/v1/users", json=request)

    # Добавили новый метод
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

# Добавляем builder для PublicUsersClient
def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())