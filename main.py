from fastapi import FastAPI
from .database import engine, metadata, database
import auth
import goods
import users

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(users.router)
app.include_router(goods.router)
app.include_router(auth.router)

# ------- without async ------#

# def get_db():
#     db = sessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get('/users/', response_model=List[ResponseUser])
#  def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users
#
#
# @app.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=ResponseUser)
#  def user_details(id: int, db: Session = Depends(get_db)):
#     necessary_user = db.query(models.User).get(id)
#
#     if necessary_user:
#         return necessary_user
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
#
#
# @app.get('/goods/', response_model=List[ResponseGood])
#  def get_goods(db: Session = Depends(get_db)):
#     goods = db.query(models.Good).all()
#     return goods
#
#
# @app.get('/goods/{id}', status_code=status.HTTP_200_OK, response_model=ResponseGood)
#  def good_details(id: int, db: Session = Depends(get_db)):
#     necessary_good = db.query(models.Good).get(id)
#
#     if necessary_good:
#         return necessary_good
#     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Good does not exist")
#
#
# @app.post('/goods/', status_code=status.HTTP_201_CREATED)
#  def add_good(good: GoodSchema, db: Session = Depends(get_db)):
#     new_good = models.Good(title=good.title, description=good.description, price=good.price, type=good.type,
#                            color_variants=good.color_variants, parametrs=good.parametrs)
#     db.add(new_good)
#     db.commit()
#     db.refresh(new_good)
#     return new_good
#
#
# @app.post('/users/', status_code=status.HTTP_201_CREATED)
#  def add_user(user: UserSchema, db: Session = Depends(get_db)):
#     new_user = models.User(name=user.name, profile_img=user.profile_img, email=user.email, password=user.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user
#
#
# @app.put('/users/{id}', status_code=status.HTTP_202_ACCEPTED)
#  def update_user(id, user: UserSchema, db: Session = Depends(get_db)):
#     db.query(models.User).filter(models.User.id == id).update(
#         {'name': user.name, 'profile_img': user.profile_img, 'email': user.email, 'password': user.password})
#     return {'message': 'User data is updated'}
#
#
# @app.put('/goods/{id}', status_code=status.HTTP_202_ACCEPTED)
#  def update_good(id, good: GoodSchema, db: Session = Depends(get_db)):
#     db.query(models.Good).filter(models.Good.id == id).update(
#         {'title': good.title, 'description': good.description, 'price': good.price, 'type': good.type,
#          'color_variants': good.color_variants, 'parametrs': good.parametrs})
#     return {'message': 'Good data is updated'}
#
#
# @app.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT)
#  def delete_user(id: int, db: Session = Depends(get_db)):
#     db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
#     db.commit()
#
#
# @app.delete('/goods/{id}', status_code=status.HTTP_204_NO_CONTENT)
#  def delete_good(id: int, db: Session = Depends(get_db)):
#     db.query(models.Good).filter(models.Good.id == id).delete(synchronize_session=False)
#     db.commit()
