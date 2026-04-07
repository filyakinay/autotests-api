from typing import TypedDict, List
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client



class Exercise(TypedDict):
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class GetCourseExercisesQueryDict(TypedDict):
    """
        Описание структуры запроса на получение списка упражнений.
    """
    courseId: str


class GetExerciseQueryDict(TypedDict):
    """
        Описание структуры запроса на получение упражнения.
    """
    exercise_id: str


class GetExerciseResponseDict(TypedDict):
    """"
        Вложенная структура упражнения
    """
    exercises: Exercise


class GetExercisesResponseDict(TypedDict):
    """"
            Вложенная структура упражнения
        """
    exercises: List[Exercise]


class CreateExerciseRequestDict(TypedDict):
    """
        Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """
        Описание структуры запроса на обновление упражнения.
    """
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExerciseClient(APIClient):
    """
        Клиент для работы с /api/v1/exercises
    """

    def get_course_exercises_api(self, query: GetCourseExercisesQueryDict) -> Response:
        """
        Метод получения списка упражнений курса.

        :param query: Словарь с exerciseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercises_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания списка упражнений курса.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title,orderIndex, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_course_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор Упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{exercise_id}")

    def get_exercises(self, query: GetCourseExercisesQueryDict) -> GetExercisesResponseDict:
        response = self.get_exercise_api(query)
        return response.json()

    def get_exercise(self,query: GetExerciseQueryDict) -> GetExerciseResponseDict:
        response = self.get_exercise_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> GetExerciseResponseDict:
        response = self.create_exercises_api(request)
        return response.json()

    def update_exercise(self, request: UpdateExerciseRequestDict) -> GetExerciseResponseDict:
        response = self.update_exercise_api(request)
        return response.json()

# Добавляем builder для CoursesClient
def get_exercises_client(user: AuthenticationUserDict) -> ExerciseClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExerciseClient(client=get_private_http_client(user))
