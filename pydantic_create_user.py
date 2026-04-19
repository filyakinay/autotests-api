from dataclasses import Field

from pydantic import BaseModel, EmailStr, constr


# Добавила модель UserSchema
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

# Добавила модель CreateUserRequestSchema
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

# Вложенная модель
class CreateUserResponseSchema(BaseModel):
    user: UserSchema
