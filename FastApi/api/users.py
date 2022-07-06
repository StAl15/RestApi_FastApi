from typing import List
from fastapi import APIRouter
from fastapi import status, HTTPException
from passlib.hash import pbkdf2_sha256
from .database import database, User
from .schemas import UserSchema, UserSchemaIn

router = APIRouter(
    tags=["Users"]
)


# тег для свагера

@router.post('/users/', response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def add_user(user: UserSchemaIn):
    hashed_password = pbkdf2_sha256.hash(user.password)
    query = User.insert().values(name=user.name, profile_img=user.profile_img, email=user.email,
                                 password=hashed_password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.get('/users/', response_model=List[UserSchema], status_code=status.HTTP_201_CREATED)
async def get_users():
    query = User.select()
    return await database.fetch_all(query=query)


@router.get('/users/{id}', response_model=UserSchema, status_code=status.HTTP_200_OK)
async def get_user_details(id: int):
    query = User.select().where(id == User.c.id)
    necessary_user = await database.fetch_one(query=query)
    if not necessary_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {**necessary_user}


@router.put('/users/{id}', response_model=UserSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_user(id: int, user: UserSchemaIn):
    hashed_password = pbkdf2_sha256.hash(user.password)
    query = User.update().where(id == User.c.id).values(name=user.name, profile_img=user.profile_img, email=user.email,
                                                        password=hashed_password)
    await database.execute(query)
    return {**user.dict(), "id": id}


@router.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    query = User.delete().where(User.c.id == id)
    await database.execute(query)
    return {"message": "User deleted"}
