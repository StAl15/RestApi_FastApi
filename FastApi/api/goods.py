from typing import List
from fastapi import APIRouter, Depends
from fastapi import status, HTTPException
from .database import database, Good
from .schemas import GoodSchema, GoodSchemaIn, UserSchema
from .token import get_current_user


router = APIRouter(
    tags=["Goods"]
)


# тег для свагера


@router.post('/goods/', response_model=GoodSchema, status_code=status.HTTP_201_CREATED)
async def add_good(good: GoodSchemaIn, current_user: UserSchema = Depends(get_current_user)):
    query = Good.insert().values(title=good.title, description=good.description, img_src=good.img_src, price=good.price,
                                 type=good.type, color_variants=good.color_variants, parametrs=good.parametrs)
    last_record_id = await database.execute(query)
    return {**good.dict(), "id": last_record_id}


@router.get('/goods/', response_model=List[GoodSchema], status_code=status.HTTP_201_CREATED)
async def get_goods(current_user: UserSchema = Depends(get_current_user)):
    query = Good.select()
    return await database.fetch_all(query=query)


@router.get('/goods/{id}', response_model=GoodSchema, status_code=status.HTTP_200_OK)
async def get_good_details(id: int, current_user: UserSchema = Depends(get_current_user)):
    query = Good.select().where(id == Good.c.id)
    necessary_good = await database.fetch_one(query=query)
    if not necessary_good:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Good not found")
    return {**necessary_good}


@router.put('/goods/{id}', response_model=GoodSchema, status_code=status.HTTP_202_ACCEPTED)
async def update_good(id: int, good: GoodSchemaIn, current_user: UserSchema = Depends(get_current_user)):
    query = Good.update().where(id == Good.c.id).values(title=good.title, description=good.description,
                                                        img_src=good.img_src, price=good.price,
                                                        type=good.type, color_variants=good.color_variants,
                                                        parametrs=good.parametrs)
    await database.execute(query)
    return {**good.dict(), "id": id}


@router.delete('/goods/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_good(id: int, current_user: UserSchema = Depends(get_current_user)):
    query = Good.delete().where(Good.c.id == id)
    await database.execute(query)
    return {"message": "Good deleted"}
