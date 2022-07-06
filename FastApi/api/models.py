# from .database import Base
# from sqlalchemy import Column, Integer, String, Float
#
# ---- without async -----#

# class Good(Base):
#     __tablename__ = "goods"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(100))
#     description = Column(String(500))
#     price = Column(Float)
#     type = Column(String(100))
#     color_variants = Column(String(100))
#     parametrs = Column(String)
#
#
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     profile_img = Column(String)
#     email = Column(String(100))
#     password = Column(String)
