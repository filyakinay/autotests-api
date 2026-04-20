from httpx import Response
from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetCourseExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, GetExerciseQuerySchema, GetExerciseResponseSchema
from clients.private_http_builder import  get_private_http_client, AuthenticationUserSchema



class ExerciseClient(APIClient):
    """
        Клиент для работы с /api/v1/exercises
    """

    def get_course_exercises_api(self, query: GetCourseExercisesQuerySchema) -> Response:
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

    def create_exercises_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания списка упражнений курса.

        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True,mode='json'))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title,orderIndex, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True,mode='json'))

    def delete_course_api(self, exercise_id: str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор Упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{exercise_id}")

    def get_exercises(self, query: GetCourseExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(query)
        return response.json()

    def get_exercise(self,query: GetExerciseQuerySchema) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestSchema) -> GetExerciseResponseSchema:
        response = self.create_exercises_api(request)
        return response.json()

    def update_exercise(self, request: UpdateExerciseRequestSchema) -> GetExerciseResponseSchema:
        response = self.update_exercise_api(request)
        return response.json()

# Добавляем builder для CoursesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExerciseClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExerciseClient(client=get_private_http_client(user))
