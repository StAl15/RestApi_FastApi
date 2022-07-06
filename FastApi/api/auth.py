from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from passlib.hash import pbkdf2_sha256
from .database import database, User
from .token import create_access_token

router = APIRouter(
    tags=["Auth"]
)


# тег для свагера

@router.post('/login/')
async def login(request: OAuth2PasswordRequestForm = Depends()):
    query = User.select().where(User.c.email == request.username)
    necessary_user = await database.fetch_one(query=query)

    if not necessary_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not pbkdf2_sha256.verify(request.password, necessary_user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid password")

    access_token = create_access_token(
        data={"sub": necessary_user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
