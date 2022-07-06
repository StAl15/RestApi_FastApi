from typing import Optional
from pydantic import BaseModel


class GoodSchemaIn(BaseModel):
    title: str
    description: str
    price: float
    type: str
    img_src: bytes
    color_variants: str
    parametrs: str


class UserSchemaIn(BaseModel):
    profile_img: bytes
    name: str
    email: str
    password: str


class GoodSchema(GoodSchemaIn):
    id: int


class UserSchema(UserSchemaIn):
    id: int
    email: str


class LoginSchema(BaseModel):
    email: str
    password: str


class TokenData(BaseModel):
    email: Optional[str] = None

# --- without async----#
# class ResponseUser(UserSchema):
#     profile_img: str
#     name: str
#     email: str
#     password: str
#
#     class Config:
#         orm_mode = True
#
#
# class ResponseGood(GoodSchema):
#     title: str
#     description: str
#     price: float
#     type: str
#     img_src: str
#     color_variants: str
#     parametrs: str
#
#     class Config:
#         orm_mode = True
