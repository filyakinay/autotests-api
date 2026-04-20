from typing import List

from pydantic import BaseModel, ConfigDict, Field


class ExerciseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)


    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias= "minScore")
    order_index: int =Field(alias="orderIndex")
    description: str
    estimatedTime: str = Field(alias="estimatedTime")


class GetCourseExercisesQuerySchema(BaseModel):
    """
        Описание структуры запроса на получение списка упражнений.
    """
    course_id: str


class GetExerciseQuerySchema(BaseModel):
    """
        Описание структуры запроса на получение упражнения.
    """
    exercise_id: str


class GetExerciseResponseSchema(BaseModel):
    """"
        Вложенная структура упражнения
    """
    exercises: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """"
            Вложенная структура упражнения
        """
    exercises: List[ExerciseSchema]


class CreateExerciseRequestSchema(BaseModel):
    """
        Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)


    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
        Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

