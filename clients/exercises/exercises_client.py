from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient

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

class CoursesClient(APIClient):
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

    def get_exercise_api(self, exercise_id:str) -> Response:
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